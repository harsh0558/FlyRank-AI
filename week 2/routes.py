from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from database import sessionLocal
from models import Tasks
from schemas import TaskSchema, UpdateTaskSchema
app = FastAPI()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/tasks")
def get_all_tasks(db: Session = Depends(get_db)):
    tasks = db.scalars(select(Tasks)).all()

    return tasks

@app.get("/task/{task_id}")
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.scalar(
        select(Tasks).where(Tasks.id == task_id)
        )

    if task is None:
        raise HTTPException(
            status_code=404,
            detail='Task not found'
        )
    
    return task

@app.post("/tasks")
def add_task(task:TaskSchema, db: Session = Depends(get_db)):
    try:
        new_task = Tasks(
            id = task.id,
            title = task.title,
            done = task.done
        )

        db.add(new_task)
        db.commit()
        db.refresh(new_task)

        return new_task
    except SQLAlchemyError as e:

        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=e
        )

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: UpdateTaskSchema, db: Session = Depends(get_db)):
    new_task = db.scalar(select(Tasks).where(Tasks.id == task_id))

    if new_task is None:
        raise HTTPException(
            status_code=404,
            detail="task not found"
        )

    try:
        new_task.title = task.title
        new_task.done = task.done

        db.commit()
        db.refresh(new_task)

        return new_task
    except SQLAlchemyError as e:

        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=e
        )

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.get(Tasks, task_id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail='Task not found'
        )

    try:
        db.delete(task)
        db.commit()

        return {
            "message": "Task deleted successfully"
            }
    except SQLAlchemyError as e:
        db.rollback()

        raise HTTPException(
            status_code=500,
            detail=e
        )