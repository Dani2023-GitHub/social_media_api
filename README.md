A RESTful API for a social media platform built with Django and Django REST Framework (DRF). This project includes user authentication, custom user profiles, and foundational features for a social media platform.

## Posts and Comments Endpoints

### Posts

- **List Posts**: `GET /api/posts/posts/`
- **Create Post**: `POST /api/posts/posts/`
- **Retrieve Post**: `GET /api/posts/posts/<id>/`
- **Update Post**: `PUT /api/posts/posts/<id>/`
- **Delete Post**: `DELETE /api/posts/posts/<id>/`

### Comments

- **List Comments**: `GET /api/posts/comments/`
- **Create Comment**: `POST /api/posts/comments/`
- **Retrieve Comment**: `GET /api/posts/comments/<id>/`
- **Update Comment**: `PUT /api/posts/comments/<id>/`
- **Delete Comment**: `DELETE /api/posts/comments/<id>/`

The authentication setup and how to test it

The Social Media API uses Token-Based Authentication provided by Django REST Framework (DRF). Each user is assigned a unique token upon successful registration or login. This token is required to access protected endpoints.

Testing Authentication

Register a user:

## POST /register/

## Body: {username, email, password}

## Response: {token}

Login: -

## POST /login/

## Body: {username, password}

## Response: {token}

Access protected endpoints:

## Add token to header: Authorization: Token <token>

## Example: GET /profile/
