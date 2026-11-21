# Task Manager API

A RESTful Task Manager API built using **Python, FastAPI, and SQLite**. This project allows users to create, view, update, delete, and filter tasks through API endpoints.

## Features

- **Create Tasks:** Add new tasks with a title, description, and completion status.
- **View Tasks:** Retrieve all tasks or fetch a specific task using its ID.
- **Update Tasks:** Modify existing task details.
- **Delete Tasks:** Remove tasks from the database.
- **Filter Tasks:** Filter tasks based on their completion status.
- **Data Persistence:** Store tasks in an SQLite database, so data remains available after restarting the server.
- **API Documentation:** Explore and test endpoints using automatically generated Swagger UI documentation.

## Tech Stack

- **Language:** Python
- **Backend Framework:** FastAPI
- **Database:** SQLite
- **Data Validation:** Pydantic
- **Server:** Uvicorn
- **Tools:** VS Code, Git, GitHub

## Project Structure

```text
task-manager-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   └── schemas.py
│
├── .gitignore
├── requirements.txt
```

*Note: The SQLite database file is generated locally and excluded from the Git repository.*

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/task-manager-api.git
```

### 2. Navigate to the project directory

```bash
cd task-manager-api
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Start the development server

```bash
python -m uvicorn app.main:app --reload
```

The API will be available at:

`http://127.0.0.1:8000`

## API Documentation

FastAPI automatically generates interactive API documentation.

Open the following URL after starting the server:

`http://127.0.0.1:8000/docs`

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/tasks` | Create a new task |
| GET | `/tasks` | Retrieve all tasks |
| GET | `/tasks/{task_id}` | Retrieve a task by ID |
| PUT | `/tasks/{task_id}` | Update an existing task |
| DELETE | `/tasks/{task_id}` | Delete a task |

### Task Filtering

You can filter tasks using the `completed` query parameter.

```http
GET /tasks?completed=true
```

```http
GET /tasks?completed=false
```

## What I Learned

Through this project, I gained practical experience with:

- Building REST APIs using FastAPI.
- Understanding HTTP methods and CRUD operations.
- Validating request data using Pydantic.
- Connecting Python applications to SQLite databases.
- Writing SQL queries for database operations.
- Handling API requests, responses, and errors.
- Testing API endpoints using Swagger UI.

## Future Improvements

- Add user authentication.
- Implement task deadlines and priority levels.
- Add automated API testing.
- Introduce pagination and additional filtering options.

---

**Developed as a hands-on project to strengthen my Python backend development skills.**
