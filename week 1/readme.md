# Task Manager API

A simple Task Manager API built with **FastAPI**. It supports basic CRUD (Create, Read, Update, Delete) operations using an in-memory list, so no database setup is required.

## Features

* View all tasks
* View a task by its ID
* Create a new task
* Update an existing task
* Delete a task
* Health check endpoint
* Interactive API documentation with Swagger UI

## Getting Started

1. Install the required packages:

```bash
pip install fastapi uvicorn
```

2. Start the server:

```bash
uvicorn main:app --reload
```

3. Open your browser and visit:

* API: `http://127.0.0.1:8000`
* Swagger UI: `http://127.0.0.1:8000/docs`

## Available Endpoints

| Method | Endpoint           | Description                 |
| ------ | ------------------ | --------------------------- |
| GET    | `/`                | Home endpoint               |
| GET    | `/tasks`           | Get all tasks               |
| GET    | `/tasks/{task_id}` | Get a task by its ID        |
| POST   | `/tasks`           | Create a new task           |
| PUT    | `/tasks/{task_id}` | Update an existing task     |
| DELETE | `/tasks/{task_id}` | Delete a task               |
| GET    | `/health`          | Check if the API is running |

## Notes

This project stores tasks in memory, which means all data is lost whenever the server is restarted. It was built as a learning project to practice building REST APIs with FastAPI and using Swagger UI for testing endpoints.
