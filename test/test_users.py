from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_register_user_invalid_username():
    response = client.post(
        "/users/register",
        json={
            "username": "ab",
            "email": "invalid_username@example.com",
            "password": "TestPassword123!",
        },
    )

    assert response.status_code == 422


def test_register_user_invalid_password():
    response = client.post(
        "/users/register",
        json={
            "username": "invalid_password_user",
            "email": "invalid_password@example.com",
            "password": "123",
        },
    )

    assert response.status_code == 422


def test_register_user_invalid_email():
    response = client.post(
        "/users/register",
        json={
            "username": "invalid_email_user",
            "email": "not-an-email",
            "password": "TestPassword123!",
        },
    )

    assert response.status_code == 422


def test_register_user_with_short_username():
    response = client.post(
        "/users/register",
        json={
            "username": "ab",
            "email": "short_username@example.com",
            "password": "TestPassword123!",
        },
    )

    assert response.status_code == 422


def test_register_user_with_short_password():
    response = client.post(
        "/users/register",
        json={
            "username": "short_password_user",
            "email": "short_password@example.com",
            "password": "123",
        },
    )

    assert response.status_code == 422

def test_register_user_with_empty_password():
    response = client.post(
        "/users/register",
        json={
            "username": "empty_password_user",
            "email": "empty_password@example.com",
            "password": "",
        },
    )

    assert response.status_code == 422

def test_register_with_username_too_long():
    response = client.post(
        "/users/register",
        json={
            "username": "a" * 51,
            "email": "long_username@example.com",
            "password": "TestPassword123!",
        },
    )

    assert response.status_code == 422


def test_register_with_password_too_long():
    response = client.post(
        "/users/register",
        json={
            "username": "long_password_user",
            "email": "long_password@example.com",
            "password": "a" * 129,
        },
    )



