# Backend - Justified Project

This is the Django-based backend for the Justified project.

## Setup Instructions

1.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```

2.  **Activate the virtual environment:**
    - Windows: `venv\Scripts\activate`
    - Linux/macOS: `source venv/bin/activate`

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Seed the database (Optional):**
    ```bash
    python seed.py
    ```

6.  **Start the server:**
    ```bash
    python manage.py runserver
    ```

## API Features

-   Django REST Framework for API endpoints.
-   CORS headers enabled for frontend integration.
-   SQLite3 database for local development.
