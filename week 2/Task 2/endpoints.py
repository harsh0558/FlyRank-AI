from contextlib import asynccontextmanager
from database import init_db
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, FastAPI
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
