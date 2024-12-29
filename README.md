# Token Manager

A Django REST API project for managing authentication tokens with admin panel control.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows: `venv\Scripts\activate`
- Unix/MacOS: `source venv/bin/activate`

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure the database:
- Create a PostgreSQL database
- Update the `.env` file with your database credentials

5. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

## Features

- Admin panel for token management (/admin)
- REST API endpoints for token operations (/api/tokens/)
- Token lifetime management
- Token invalidation
- User-specific token tracking

## API Endpoints

- `GET /api/tokens/` - List all tokens (admin only)
- `POST /api/tokens/` - Create a new token
- `GET /api/tokens/{id}/` - Retrieve a specific token
- `PUT /api/tokens/{id}/` - Update a token
- `DELETE /api/tokens/{id}/` - Delete a token
