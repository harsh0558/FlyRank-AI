import uuid
from sqlalchemy import select,UUID
from models import Task
from sqlalchemy.ext.asyncio import AsyncSession
from schemas import createTaskSchema

class CRUD:

    async def get_all_tasks(self,session:AsyncSession)->list[Task]:
        result = await session.execute(select(Task))
        tasks = list(result.scalars().all())
        return tasks

    async def get_task(self, id:uuid.UUID, session:AsyncSession):
        result = await session.execute(select(Task).where(Task.id == id))
        task = result.scalar_one_or_none()
        return task

    async def create_task(self, user_task:createTaskSchema, session: AsyncSession)->Task:
        task = Task(title=user_task.title, done=user_task.done)
        session.add(task)
        await session.commit()
        return task

    async def update_task(self, id:uuid.UUID, user_task:createTaskSchema, session:AsyncSession)->Task|None:
        result = await session.execute(select(Task).where(Task.id == id))
        task = result.scalar_one_or_none()
        if task is not None:
            task.title = user_task.title
            task.done = user_task.done

        await session.commit()
        return task

    async def delete_task(self, id:uuid.UUID, session:AsyncSession) -> bool:
        result = await session.execute(select(Task).where(Task.id == id))
        task = result.scalar_one_or_none()

        if task is None:
            return False

        await session.delete(task)
        await session.commit()

        return True

    