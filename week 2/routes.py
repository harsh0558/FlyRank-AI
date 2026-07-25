from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from database import sessionLocal
from models import Tasks
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