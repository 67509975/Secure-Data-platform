# Secure Data Platform API - Threat Model

## 1. Purpose

This threat model identifies potential security threats affecting the Secure Data Platform API and documents the controls implemented to reduce those risks.

The assessment focuses on authentication, authorization, input validation, sensitive data protection, and API security.

## 2. System Overview

The Secure Data Platform API is a FastAPI-based REST API that provides:

- User registration
- User authentication
- JWT-based authentication
- User profile access
- Administrative user management
- PostgreSQL database storage

### Main Components

- FastAPI application
- PostgreSQL database
- SQLAlchemy ORM
- JWT authentication
- Password hashing using pwdlib
- Automated security tests

## 3. Assets

The primary assets are:

| Asset | Description |
|---|---|
| User credentials | User passwords and authentication information |
| Password hashes | Stored password hashes |
| JWT tokens | Authentication credentials |
| User data | Usernames, email addresses and account status |
| Database | Persistent application data |
| Admin functionality | Privileged administrative operations |
| Application secrets | JWT signing key and database credentials |

## 4. Trust Boundaries

### Client → API

Users interact with the API through HTTP requests.

The API must not trust:

- User input
- Authorization headers
- JWT tokens
- Requested user roles

### API → Database

The API communicates with PostgreSQL through SQLAlchemy.

Database errors must not expose internal implementation details to clients.

## 5. Threats and Controls

| Threat | Risk | Security Control |
|---|---|---|
| Credential theft | High | Password hashing |
| Brute-force login attempts | Medium | Authentication controls |
| Invalid JWT | High | JWT signature validation |
| Expired JWT | High | JWT expiration validation |
| Privilege escalation | High | Server-side role assignment |
| Unauthorized admin access | High | Role-based access control |
| Password exposure | High | Response schemas exclude passwords |
| Database error disclosure | Medium | Controlled database exception handling |
| Malicious input | High | Pydantic input validation |
| Inactive account access | Medium | Account status verification |

## 6. Authentication

Authentication uses:

- Username and password credentials
- Password hashing
- JWT access tokens
- JWT expiration
- Bearer token authentication

Invalid, malformed, tampered, random, and expired tokens are rejected.

## 7. Authorization

Role-based access control is implemented for administrative functionality.

Normal users cannot access:

`GET /admin/users`

Administrative access requires the authenticated user's role to be:

`admin`

Users cannot assign themselves an administrative role during registration.

## 8. Sensitive Data Protection

The API uses `UserResponse` to control the fields returned to clients.

The following values are never returned through user response endpoints:

- Password
- Password hash

Database errors are also converted into controlled application responses rather than exposing raw database exceptions.

## 9. Security Testing

Automated tests cover:

- Invalid JWT
- Missing JWT
- Malformed authorization headers
- Empty bearer tokens
- Tampered JWT
- Expired JWT
- Incorrect authorization schemes
- Unauthorized admin access
- Privilege escalation attempts
- Input validation
- Duplicate registration
- Password exposure
- Inactive account login
- Unsupported HTTP methods

## 10. Future Security Improvements

Planned improvements include:

- Rate limiting
- Refresh token strategy
- Stronger password policy
- Security headers
- Structured security logging
- Dependency vulnerability scanning
- Static security analysis
- Container security
- CI/CD security gates
- Penetration testing