from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_admin_users_without_token():
    response = client.get("/admin/users")

    assert response.status_code == 401


def test_admin_users_with_invalid_token():
    response = client.get(
        "/admin/users",
        headers={
            "Authorization": "Bearer invalid-token",
        },
    )

    assert response.status_code == 401

def test_admin_endpoint_rejects_random_token():
    response = client.get(
        "/admin/users",
        headers={
            "Authorization": "Bearer 123456789",
        },
    )

    assert response.status_code == 401


def test_admin_endpoint_rejects_basic_auth():
    response = client.get(
        "/admin/users",
        headers={
            "Authorization": "Basic dXNlcjpwYXNzd29yZA==",
        },
    )

    assert response.status_code == 401


def test_admin_endpoint_rejects_wrong_scheme():
    response = client.get(
        "/admin/users",
        headers={
            "Authorization": "Token fake-token",
        },
    )

    assert response.status_code == 401

def test_normal_user_cannot_access_admin_users():
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
        "/admin/users",
        headers={
            "Authorization": f"Bearer {token}",
        },
    )

    assert response.status_code == 403

def test_admin_users_requires_authentication():
    response = client.get("/admin/users")

    assert response.status_code == 401


def test_admin_users_rejects_invalid_token():
    response = client.get(
        "/admin/users",
        headers={"Authorization": "Bearer invalid-token"},
    )

    assert response.status_code == 401


def test_normal_user_cannot_access_admin_users():
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
        "/admin/users",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 403