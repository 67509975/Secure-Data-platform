# Secure Data Platform

A production-oriented data platform built with **Python and FastAPI**, with a focus on **secure REST API development, application security, and DevSecOps practices**.

The project demonstrates how data can be securely **collected, validated, processed, stored, and exposed through APIs**, while applying security principles throughout the software development lifecycle.

> **Status:** Completed


---

## 🎯 Project Objective

The goal of this project is to build a secure, production-oriented data platform from the ground up.

The platform is being developed incrementally, beginning with a secure REST API foundation and expanding toward broader data engineering and cloud capabilities.

The project focuses on:

* Secure REST API development
* Authentication and authorization
* Role-based access control
* Data validation and protection
* Database design and management
* Automated testing
* Security testing
* Dependency vulnerability management
* CI/CD and DevSecOps
* Data ingestion and transformation
* Data quality and reliability
* Cloud infrastructure
* Security monitoring and auditing

Security is incorporated throughout the platform rather than treated as a separate component.

---

## 🏗️ Current Architecture

The current implementation focuses on the secure API and database layer:

```text
                    Client
                       │
                       ▼
              ┌─────────────────┐
              │     FastAPI     │
              │    REST API     │
              └────────┬────────┘
                       │
              ┌────────▼────────┐
              │   Security      │
              │ Authentication  │
              │ Authorization   │
              │ Validation      │
              └────────┬────────┘
                       │
              ┌────────▼────────┐
              │   SQLAlchemy    │
              │      ORM        │
              └────────┬────────┘
                       │
              ┌────────▼────────┐
              │   PostgreSQL    │
              │ Operational Data│
              └─────────────────┘

---

# 🔐 Security

Security is a core design consideration of the platform.

### Authentication

The API implements JWT-based authentication with:

* Secure password hashing
* Login authentication
* JWT access tokens
* Protected API endpoints
* Authentication failure handling
* Inactive-user checks

### Authorization

Role-based access control (RBAC) is implemented to restrict administrative functionality.

The API distinguishes between normal users and administrators and prevents unauthorized users from accessing administrative endpoints.

### Input Validation

Request data is validated using Pydantic schemas, including:

* Username validation
* Password requirements
* Email validation
* Required fields
* Response validation

### Database Security

The application uses:

* PostgreSQL
* SQLAlchemy
* Database sessions
* Unique constraints
* Environment-based database configuration
* Separate test database configuration

### Additional Security Practices

The project incorporates:

* Least-privilege principles
* Secure error handling
* Secrets management
* Dependency vulnerability scanning
* Security testing
* CI/CD security checks
* Threat modelling
* Penetration testing
* Container security

---

# 🧪 Security & Automated Testing

Security is integrated into the development workflow through automated testing and security scanning.

### Pytest

The project contains automated tests covering areas including:

* API health
* User registration
* Authentication
* JWT-protected endpoints
* User access
* Administrative access
* Role-based authorization
* Invalid credentials
* Validation failures
* Duplicate users
* Inactive users
* Security-related API behaviour

Run the tests with:

```bash
python -m pytest -q
```

### Bandit

Bandit is used for static security analysis of the Python application:

```bash
bandit -r app
```

### pip-audit

Dependency vulnerabilities are checked using:

```bash
pip-audit
```

### Dependency Verification

Python dependency consistency can be checked with:

```bash
python -m pip check
```

---

# ⚙️ DevSecOps / CI/CD

The project uses GitLab CI/CD to automate testing and security checks.

The current pipeline contains:

```text
Test
  │
  ▼
Security
  ├── Bandit
  └── pip-audit
```

The pipeline automatically:

1. Sets up the Python environment
2. Installs project dependencies
3. Runs the automated test suite
4. Performs static security analysis
5. Audits Python dependencies

Current `.gitlab-ci.yml` stages:

```yaml
stages:
  - test
  - security
```

This demonstrates a **shift-left security approach**, integrating security checks into the development and CI/CD process.

---

# 🛡️ Threat Modelling & Security Documentation

Security risks are considered during the design and development of the platform.

The project includes documentation covering:

* Threat modelling
* Authentication threats
* Authorization risks
* Credential protection
* Input validation
* API security
* Database security
* Dependency vulnerabilities
* Security testing

Security documentation is maintained under:

```text
security/
```

---

# 📬 API Testing

Postman is used to test the REST API and demonstrate its security controls.

The API workflow includes:

```text
Register User
     │
     ▼
Login
     │
     ▼
Receive JWT
     │
     ▼
Access Protected Endpoint
     │
     ▼
Attempt Unauthorized Admin Access
     │
     ▼
403 Forbidden
     │
     ▼
Authenticate as Admin
     │
     ▼
Access Admin Endpoint
```

FastAPI's interactive documentation is also available through Swagger UI when the application is running:

```text
http://localhost:8000/docs
```

---

# 🛠️ Technology Stack

## Current

* Python 3.12
* FastAPI
* Uvicorn
* PostgreSQL
* SQLAlchemy
* Pydantic
* JWT
* pwdlib
* Pytest
* Bandit
* pip-audit
* Git
* GitHub
* GitLab CI/CD
* Postman

## Planned

* Docker
* Cloud infrastructure
* Azure
* ETL / ELT tooling
* Data warehouse technologies
* Analytics / BI
* Security monitoring and observability

---

# 📂 Project Structure

```text
secure-data-platform/
│
├── app/
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│   │
│   ├── database/
│   │   └── dependencies.py
│   │
│   ├── models/
│   │   └── user.py
│   │
│   ├── routers/
│   │   ├── auth.py
│   │   ├── users.py
│   │   └── admin.py
│   │
│   ├── schemas/
│   │   ├── auth.py
│   │   └── user.py
│   │
│   └── main.py
│
├── security/
│   ├── threat-model.md
│   └── penetration-test-report.md
│
├── test/
│   ├── conftest.py
│   ├── test_health.py
│   ├── test_security.py
│   ├── test_users.py
│   └── test_admin.py
│
├── .gitlab-ci.yml
├── Dockerfile
├── .dockerignore
├── requirements.txt
├── requirements-dev.txt
└── README.md
```

---

# 🚧 Project Status

**Status: In Development**

The project is being developed incrementally.

### Current milestone

The current implementation establishes the secure REST API foundation, including:

* FastAPI REST API
* PostgreSQL database
* SQLAlchemy ORM
* User registration
* Password hashing
* JWT authentication
* Role-based access control
* Input validation
* Automated testing
* Security testing
* Threat modelling
* Dependency security scanning
* GitLab CI/CD security checks

### Next development areas

The platform will progressively expand into:

* Containerisation
* Cloud deployment
* Data ingestion
* ETL / ELT pipelines
* Data quality controls
* Data warehousing
* Analytics
* Monitoring and auditing

---

# 📚 Learning Objectives

This project is intended to demonstrate practical experience in:

* Backend development
* REST API architecture
* Application security
* Authentication and authorization
* Database engineering
* Secure software development
* Automated testing
* Security testing
* DevSecOps
* CI/CD
* Data engineering
* Cloud engineering
* Production-oriented software development

---

# 👤 Author

**Tshegofatso Khoza**

Software Engineering | Security Engineering | DevSecOps
