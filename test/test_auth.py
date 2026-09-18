from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_login_success():
    response = client.post(
        "/auth/login",
        data={
            "username": "login_test_user",
            "password": "TestPassword123!",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_wrong_password():
    response = client.post(
        "/auth/login",
        data={
            "username": "login_test_user",
            "password": "WrongPassword123!",
        },
    )

    assert response.status_code == 401


def test_users_me_without_token():
    response = client.get("/users/me")

    assert response.status_code == 401


def test_users_me_with_valid_token():
    response = client.post(
        "/auth/login",
        data={
            "username": "login_test_user",
            "password": "TestPassword123!",
        },
    )

    assert response.status_code == 200

    token = response.json()["access_token"]

    response = client.get(
        "/users/me",
        headers={
            "Authorization": f"Bearer {token}",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["username"] == "login_test_user"
    assert data["email"] == "login_test@example.com"