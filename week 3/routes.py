from fastapi import FastAPI
from contextlib import asynccontextmanager
from supabase import acreate_client, AsyncClient
from dotenv import load_dotenv
import os
load_dotenv()

url:str = str(os.getenv("SUPABASE_PROJECT_URL"))
key:str = str(os.getenv("SUPABASE_PUBLIC_KEY"))


@asynccontextmanager
async def lifespan(app: FastAPI):
    supabase_client:AsyncClient = await acreate_client(
        supabase_url=url,
        supabase_key=key
    )

    app.state.supabase = supabase_client

    yield

app = FastAPI(lifespan=lifespan)
