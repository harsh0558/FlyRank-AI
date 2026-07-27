from contextlib import asynccontextmanager
from schemas import createTaskSchema, createTaskResponse
from database import init_db
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, FastAPI, HTTPException, status
import uuid
from CRUD import CRUD
from database import sessionLocal

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(lifespan=lifespan)

crud = CRUD()

async def get_db():
    db =  sessionLocal()
    try:
        yield db
    finally:
        await db.close()

@app.get("/tasks")
async def get_tasks(db: AsyncSession = Depends(get_db)):
    result =  await crud.get_all_tasks(db)
    return result

@app.get("/tasks/{task_id}")
async def get_task(task_id:uuid.UUID,db: AsyncSession = Depends(get_db)):
    result = await crud.get_task(task_id,db)
    if result is None:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    return result

@app.post("/tasks", response_model=createTaskResponse)
async def create_task(task:createTaskSchema, db: AsyncSession = Depends(get_db)):
    result = await crud.create_task(task,db)
    return result

@app.put("/tasks/{task_id}", response_model=createTaskResponse)
async def update_task(task_id:uuid.UUID, task:createTaskSchema, db: AsyncSession = Depends(get_db)):
    result = await crud.update_task(task_id, task, db)

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="invalid task id"
        )

    return result

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
        result = await crud.delete_task(task_id, db)

        if result is False:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="invalid task id"
            )

        return {
            "result":"task succesfully deleted"
        }