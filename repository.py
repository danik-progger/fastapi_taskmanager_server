from data import new_session, TaskORM
from classes import Task, STask
from sqlalchemy import select


class TasksRepository:
    @classmethod
    async def add_one(cls, data: Task) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()
            task = TaskORM(**task_dict)

            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def get_all(cls) -> list[STask]:
        async with new_session() as session:
            query = select(TaskORM)
            result = await session.execute(query)
            tasks_models = result.scalars().all()
            tasks = [*tasks_models]
            return tasks
