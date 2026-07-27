# Database-Backed Task Manager API (SQLite & FastAPI)

A persistent RESTful CRUD API built with **Python**, **FastAPI**, and **SQLite** (using SQLAlchemy ORM). Unlike in-memory applications, all task data is stored in a SQLite database file, enabling complete data persistence across application restarts.

---

## 🚀 Features & Architecture

* **Database Persistence**: Fully backed by SQLite (`tasks.db`). Data survives server restarts.
* **Automatic Database & Table Creation**: Opening/initializing the database automatically creates `tasks.db` and the `tasks` schema if it does not exist.
* **RESTful CRUD Operations**: Full support for listing, fetching by ID, creating, updating, and deleting tasks.
* **Parameterized Queries / ORM Safety**: Protects against SQL injection by using parameterized queries / SQLAlchemy ORM mappings.

---

## 🛠️ Why SQLite?

1. **Single File Storage**: The entire database resides in a single file (`tasks.db`).
2. **Zero Setup / Configuration**: No separate database engine, user credentials, or server processes to install and configure.
3. **Data Persistence**: Data easily outlives the application process—restarting the API retains all changes.

---

## 📁 Database File Location & Behavior

* **File Location**: `tasks.db` (located in the root project / project directory).
* **Automatic Creation**: Created automatically on first app startup when the database engine connects.
* **Git-Ignored**: Added to `.gitignore` so each environment/clone starts clean with auto-seeded initial data.

---

## ⚡ Quick Start / How to Run

### 1. Install Dependencies
```bash
pip install -r requirements.txt
# Or install directly:
pip install fastapi uvicorn sqlalchemy pydantic
```

### 2. Run the Application
Run the following single command to launch the API server:

```bash
uvicorn routes:app --reload
```

> **Zero Manual Setup**: On launching the command, `tasks.db` is created automatically (if not already present), the `tasks` table schema is applied, and 3 initial example tasks are seeded once.

---

## 📡 API Endpoints & CRUD Matrix

| Method | Endpoint | Description | Success Code | Error Code |
| :--- | :--- | :--- | :--- | :--- |
| **GET** | `/tasks` | Retrieve all tasks from database | `200 OK` | `500` |
| **GET** | `/task/{id}` | Retrieve single task by ID | `200 OK` | `404 Not Found` |
| **POST** | `/tasks` | Create a new task (auto-increment ID) | `201 Created` | `400 Bad Request` |
| **PUT** | `/tasks/{id}` | Update title or completion status (`done`) | `200 OK` | `404 Not Found / 400` |
| **DELETE** | `/tasks/{id}` | Delete task by ID | `200 OK / 204 No Content` | `404 Not Found` |

---

## 🔍 Database Inspection & SQL Verification (Stage 4)

You can view and execute raw SQL queries directly against `tasks.db` using **DB Browser for SQLite**.

### Example SQL Query Executed:
```sql
SELECT * FROM tasks WHERE done = 1;
```
* **Query Description**: Retrieves all tasks where the `done` status is set to completed (`1`).
* **Execution Output**:
  ```text
  id | title | done
  ---+-------+-----
   3 | task3 | 1
  ```
*(The API and DB Browser read and write to the exact same single source of truth (`tasks.db`), reflecting changes instantly without needing a server restart).*


## 🧪 Testing Verification & Checkpoints

1. **Persistence Checkpoint**: Created new tasks via `POST /tasks`, stopped the server, restarted it, and verified via `GET /tasks` that created tasks persisted.
2. **CRUD & HTTP Status Codes**:
   - `POST /tasks` -> `201 Created`
   - `GET /tasks` -> `200 OK`
   - `PUT /tasks/{id}` -> `200 OK`
   - `DELETE /tasks/{id}` -> `200 OK` / `204 No Content`
   - Invalid / Non-existent ID queries -> `404 Not Found` (`{"detail": "Task not found"}`)
