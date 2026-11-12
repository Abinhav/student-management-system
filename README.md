# Student Management System

A full-stack Student Management System built using Python, FastAPI, PostgreSQL, HTML, CSS, and JavaScript.

## Features

- Add new students
- View all students
- Update student details
- Delete students
- Email validation
- Duplicate email prevention
- Database integration
- REST API error handling
- CORS configuration

## Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python, FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy

## Project Structure

```text
student-management/
├── backend/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── .env
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── .gitignore
└── README.md
```

## How to Run

1. Activate the Python virtual environment.
2. Install the required Python packages.
3. Configure PostgreSQL credentials in `backend/.env`.
4. Start the FastAPI server.
5. Open the frontend in your browser.

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/students` | Add student |
| GET | `/students` | View students |
| PUT | `/students/{id}` | Update student |
| DELETE | `/students/{id}` | Delete student |

## Project Status

Completed basic CRUD operations, frontend integration, database connectivity, input validation, and error handling.