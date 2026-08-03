from fastapi import FastAPI,status
from contextlib import asynccontextmanager
from supabase_client import create_supabase_client
from routes import router
from register_exceptions import register_exception_handlers

@asynccontextmanager
async def lifespan(
    app: FastAPI
):
    client = await create_supabase_client()
    app.state.supabase = client
    yield

app = FastAPI(
    lifespan=lifespan
)

register_exception_handlers(app)
app.include_router(router)