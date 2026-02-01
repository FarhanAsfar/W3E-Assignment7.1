# Task Manager (Flask + PostgreSQL)

A basic task manager backend built with **Flask**, **PostgreSQL (Docker)**, **SQLAlchemy**, and **Flask-Migrate**.

This README only covers **project setup** so anyone can clone and run the project locally.

---

## Prerequisites

Make sure you have the following installed:

- Python **3.10+**
- Docker & Docker Compose
- Git

Verify installations:

```bash
python3 --version
docker --version
docker-compose --version


Project Setup
1. Clone the repository

```bash
git clone <your-repo-url>
cd <project-folder>

2. Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Create .env file

Create a .env file in the project root:
```bash
FLASK_ENV=development
DATABASE_URL=postgresql://postgres:postgres@localhost:5433/task_manager_db

5. Start PostgreSQL using Docker
docker-compose up -d

6. Set Flask application entry point
export FLASK_APP=run.py


7. Initialize database migrations (one-time)
flask db init

8. Start the Flask server
python3 run.py


You should see:

Running on http://127.0.0.1:5000


Verify Database Connection

Enter the Postgres container:

docker exec -it <postgres_container_name> psql -U postgres -d task_manager_db

List databases or tables:

\l
\dt