# Task 2 - FastAPI Task Management API with PostgreSQL & Docker

An asynchronous RESTful API built with **FastAPI**, **SQLAlchemy (Async)**, and **PostgreSQL**, managed using **Docker Compose**.

---

## 🛠️ Prerequisites

- [Python 3.11+](https://www.python.org/)
- [Docker](https://www.docker.com/) & Docker Compose

---

## 🚀 Getting Started

### 1. Environment Configuration
Copy the example environment file to create your local `.env`:
```bash
cp .env.example .env
```

Default connection string in `.env`:
```env
POSTGRES_URL="postgresql+asyncpg://postgres:dev@localhost:5432/tasks"
```

---

### 2. Start PostgreSQL Database

Start the PostgreSQL container using Docker Compose:
```bash
docker compose up -d
```

To verify the container is running:
```bash
docker compose ps
```

---

### 3. Install Dependencies & Run FastAPI

Install Python dependencies:
```bash
pip install -r requirements.txt
```

Start the FastAPI application:
```bash
uvicorn endpoints:app --reload
```

The server will start at `http://127.0.0.1:8000`.

---

## 📖 API Documentation

FastAPI automatically generates interactive Swagger documentation.

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### Endpoints Overview

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/tasks` | Retrieve all tasks |
| `GET` | `/tasks/{task_id}` | Retrieve a single task by UUID |
| `POST` | `/tasks` | Create a new task |
| `PUT` | `/tasks/{task_id}` | Update an existing task |
| `DELETE` | `/tasks/{task_id}` | Delete a task by UUID |

---

## 🐳 Docker Commands Reference

| Command | Action |
| :--- | :--- |
| `docker compose up -d` | Start services in background |
| `docker compose logs -f` | Tail container logs |
| `docker compose down` | Stop services |
| `docker compose down -v` | Stop services and remove persistent volumes |