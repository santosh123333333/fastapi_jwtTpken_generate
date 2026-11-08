# fastapi_jwtTpken_generate
# FastAPI JWT Token Generator

A simple and secure JWT (JSON Web Token) authentication system built using **FastAPI, Python, and SQLAlchemy**.

## Features

- User Registration
- User Login & Authentication
- JWT Access Token Generation
- Password Hashing using Bcrypt
- JWT Token Verification
- Protected API Endpoints
- Token Expiration
- SQLite Database Integration
- Swagger API Documentation

## Project Structure

```text
fastapi_jwtTpken_generate/
│
├── app/
│   └── main.py
│
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/santosh123333333/fastapi_jwtTpken_generate.git
```

### 2. Navigate to Project

```bash
cd fastapi_jwtTpken_generate
```

### 3. Create Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure Environment Variables

Create a `.env` file using `.env.example`.

```env
SECRET_KEY=your-secret-key
ACCESS_TOKEN_EXPIRE_MINUTES=30
DATABASE_URL=sqlite:///./users.db
```

### 7. Run FastAPI Application

```bash
uvicorn app.main:app --reload
```

## API Documentation

Once the application is running, open:

- **API URL:** http://127.0.0.1:8000
- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/auth/register` | Register New User |
| POST | `/auth/login` | Login & Generate JWT |

## Authentication Workflow

1. Register a new user with email and password.
2. Login using registered credentials.
3. Receive a JWT access token.
4. Add the token to the Authorization header.
5. Access protected API endpoints.

### Authorization Header

```http
Authorization: Bearer YOUR_ACCESS_TOKEN
```

## Technologies Used

- Python
- FastAPI
- SQLAlchemy
- PyJWT
- Passlib
- Bcrypt
- SQLite
- OAuth2

## Security

- Passwords are securely hashed.
- JWT tokens are digitally signed.
- Expired tokens are rejected.
- Protected routes require authentication.
- Secret keys should be stored securely in environment variables.

## Future Improvements

- Refresh Token Authentication
- Password Reset
- Role-Based Authentication
- User Logout & Token Revocation
- PostgreSQL Integration

## Author

**Santosh**

GitHub: [@santosh123333333](https://github.com/santosh123333333)

Repository: [fastapi_jwtTpken_generate](https://github.com/santosh123333333/fastapi_jwtTpken_generate)

## License

This project is open source and available for learning and development.
