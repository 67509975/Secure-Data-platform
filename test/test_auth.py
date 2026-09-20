import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from app.core.config import settings
from app.core.security import hash_password
from app.database.database import Base
from app.database.dependencies import get_db
from app.main import app
from app.models.user import User


test_engine = create_engine(
    settings.test_database_url,
    pool_pre_ping=True,
    poolclass=NullPool,
)
TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=test_engine,
)


@pytest.fixture(scope="session", autouse=True)
def setup_test_database():
    Base.metadata.create_all(bind=test_engine)

    yield

    Base.metadata.drop_all(bind=test_engine)


@pytest.fixture
def db_session():
    db = TestingSessionLocal()

    try:
        yield db
    finally:
        db.close()


@pytest.fixture
def login_test_user(db_session):
    existing_user = (
        db_session.query(User)
        .filter(User.username == "login_test_user")
        .first()
    )

    if existing_user:
        db_session.delete(existing_user)
        db_session.commit()

    user = User(
        username="login_test_user",
        email="login_test@example.com",
        hashed_password=hash_password("TestPassword123!"),
        role="user",
        is_active=True,
    )

    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)

    return user


@pytest.fixture
def client(db_session):
    def override_get_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()

def test_users_me_does_not_expose_password(client, login_test_user):
    login_response = client.post(
        "/auth/login",
        data={
            "username": "login_test_user",
            "password": "TestPassword123!",
        },
    )

    assert login_response.status_code == 200

    token = login_response.json()["access_token"]

    response = client.get(
        "/users/me",
        headers={
            "Authorization": f"Bearer {token}",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert "password" not in data
    assert "hashed_password" not in data