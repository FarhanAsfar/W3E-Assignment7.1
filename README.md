# Task Manager (Flask + PostgreSQL)

A basic task manager application built with **Flask**, **PostgreSQL (Docker)**, **SQLAlchemy**, and **Flask-Migrate**, and **Jinja Templates**.

---

## Tech Stack
- Backend: Flask

- ORM: SQLAlchemy

- Migrations: Flask-Migrate (Alembic)

- Database: PostgreSQL (Docker)

- Frontend: Jinja Templates (HTML)

--- 

## Features

- Create, read, update, delete tasks

- Due date validation (cannot set past dates)

- Filter tasks by status 

- Search tasks by title or description (using query param)

- Sort tasks by due date or creation date

- Toggle task status (Mark Done / Mark Undone)

---

## Project Setup

### Prerequisites

Make sure you have the following installed:
```
- Python **3.10+**
- Docker & Docker Compose
- Git
```

Verify installations:

```bash
python3 --version
docker --version
docker-compose --version
```

### Setup Steps

**1. Clone the repository**

```bash
git clone <your-repo-url>
cd <project-folder>
```

**2. Create and activate virtual environment**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Create .env file**
Create a .env file in the project root:
```bash
FLASK_ENV=development
DATABASE_URL=postgresql://postgres:postgres@localhost:5433/task-db 
```
> *Here, I have provided with the actual database url. It is only for the assignment checking purpose and it is just a mock db url. However, It is not the best practice and should be avoided.*

**5. Start PostgreSQL using Docker**
```bash
docker-compose up -d
```
Confirm container is running:
```
docker ps
```

**6. Set Flask application entry point**
```bash
export FLASK_APP=run.py
```

**7. Initialize database migrations (one-time)**
```bash
flask db init
flask db migrate -m "Initial tables"
flask db upgrade
```

**8. Start the Flask server**
```bash
python3 run.py
```

You should see:
```
Running on http://127.0.0.1:5000
```

**Verify Database Connection**

Enter the Postgres container:
```
docker exec -it <postgres_container_name> psql -U postgres -d task-db
```
List databases or tables:
```
\l

\dt
```

---
## REST API Endpoints

**Base URL:** `/api/v1/tasks`
| Method | Endpoint            | Description       |
| ------ | ------------------- | ----------------- |
| POST   | `/create-task`      | Create a new task |
| GET    | `/`                 | Get all tasks     |
| GET    | `/task-by-id/<id>`  | Get task by ID    |
| PUT    | `/edit-task/<id>`   | Update task       |
| DELETE | `/delete-task/<id>` | Delete task       |

--- 

## Query Parameters (GET /api/v1/tasks)

`status=todo|in_progress|done`

`q=search_text`

`sort=due_date|created_at`

---

### Task Model
```bash
Task:
- id (int)
- title (string)
- description (text)
- status (enum: todo, in_progress, done)
- due_date (date)
- created_at (timestamp)
```
---

### Logging

All task operations are logged

Logs include:

- Task creation

- Updates

- Deletions

- Status toggles

Logs are saved in the `logs` folder which will be automatically created, and also shows in the console.

--- 

## Improvements
- Can add middleware token to access the routes
- Can add pagination for the tasks page
- Can use Global response and error handler and avoid repeating try/except
- Can add tests for better error handling and bug fixing

---

## Frontend Page Views

- Home Page
<img width="1286" height="801" alt="home" src="https://github.com/user-attachments/assets/e944b731-cdb3-445f-b9e5-86c313626036" />

- Tasks List Page
<img width="1274" height="741" alt="tasks" src="https://github.com/user-attachments/assets/22a35ccf-eb91-4c66-9313-dba21f56adb3" />

- Filtering Tasks with 'done' Status
<img width="1180" height="540" alt="sort-done" src="https://github.com/user-attachments/assets/f88cf6d3-0bf9-4cd5-bcf6-a7329869a20a" />

- Filtering Tasks by Sorting Date
<img width="1180" height="540" alt="sort-date" src="https://github.com/user-attachments/assets/7cd56a5e-df00-4aba-8b0d-a720e55c4f8a" />

