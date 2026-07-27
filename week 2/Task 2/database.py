from sqlalchemy import select

from config import db_config
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from models import Base, Task
from tasks import tasks

url = db_config.Postgres_URL

engine = create_async_engine(
    url=url,
    echo=True
)

sessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession
)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with sessionLocal() as session:
        result = await session.execute(select(Task).limit(1))
        task = result.scalar_one_or_none()

        if task is None:
            session.add_all(tasks)
            await session.commit()

