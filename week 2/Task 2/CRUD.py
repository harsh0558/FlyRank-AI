from sqlalchemy import select
from models import Task
from sqlalchemy.ext.asyncio import AsyncSession
class CRUD:
    async def get_all_tasks(self,session:AsyncSession):
        result = await session.execute(select(Task))
        tasks = result.scalars().all()

        return tasks

    