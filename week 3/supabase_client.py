from supabase import (
    acreate_client,
    AsyncClient,
)
from dotenv import load_dotenv
import os


load_dotenv()

url:str = str(os.getenv("SUPABASE_PROJECT_URL"))
key:str = str(os.getenv("SUPABASE_PUBLIC_KEY"))

async def create_supabase_client():
    supabase_client:AsyncClient = await acreate_client(
            supabase_url=url,
            supabase_key=key
        )

    return supabase_client

