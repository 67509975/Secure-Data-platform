from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_invalid_jwt_is_rejected():
    response = client.get(
        "/users/me",
        headers={
            "Authorization": "Bearer invalid.jwt.token",
        },
    )

    assert response.status_code == 401


def test_missing_jwt_is_rejected():
    response = client.get("/users/me")

    assert response.status_code == 401


def test_malformed_authorization_header_is_rejected():
    response = client.get(
        "/users/me",
        headers={
            "Authorization": "NotBearer token",
        },
    )

    assert response.status_code == 401


def test_empty_bearer_token_is_rejected():
    response = client.get(
        "/users/me",
        headers={
            "Authorization": "Bearer ",
        },
    )

    assert response.status_code == 401


def test_invalid_jwt_cannot_access_admin_endpoint():
    response = client.get(
        "/admin/users",
        headers={
            "Authorization": "Bearer invalid.jwt.token",
        },
    )

    assert response.status_code == 401

def test_missing_jwt_cannot_access_admin_endpoint():
    response = client.get("/admin/users")

    assert response.status_code == 401

def test_random_string_token_is_rejected():
    response = client.get(
        "/users/me",
        headers={
            "Authorization": "Bearer 123456789",
        },
    )

    assert response.status_code == 401


def test_tampered_jwt_is_rejected():
    response = client.get(
        "/users/me",
        headers={
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.tampered.signature",
        },
    )

    assert response.status_code == 401


def test_basic_auth_is_rejected():
    response = client.get(
        "/users/me",
        headers={
            "Authorization": "Basic dXNlcjpwYXNzd29yZA==",
        },
    )

    assert response.status_code == 401


def test_wrong_authorization_scheme_is_rejected():
    response = client.get(
        "/users/me",
        headers={
            "Authorization": "Token some-token",
        },
    )

    assert response.status_code == 401

def test_users_me_does_not_accept_post():
    response = client.post("/users/me")

    assert response.status_code in [405, 401]


def test_admin_users_does_not_accept_post():
    response = client.post("/admin/users")

    assert response.status_code in [405, 401]


def test_health_does_not_accept_post():
    response = client.post("/health")

    assert response.status_code == 405

def test_tampered_jwt_is_rejected():
    response = client.get(
        "/users/me",
        headers={
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.tampered.signature",
        },
    )

    assert response.status_code == 401

def test_tampered_jwt_is_rejected():
    response = client.get(
        "/users/me",
        headers={
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.tampered.signature",
        },
    )

    assert response.status_code == 401

def test_health_does_not_accept_post():
    response = client.post("/health")

    assert response.status_code == 405


def test_admin_users_does_not_accept_post():
    response = client.post("/admin/users")

    assert response.status_code in [401, 405]
