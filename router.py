from typing import Annotated
from fastapi import APIRouter, Depends
from classes import Task, STask, TaskStatus
from repository import TasksRepository

router = APIRouter(
    prefix="/tasks",
    tags=["Таски"]
)


@router.post("")
async def create_task(task: Annotated[Task, Depends()]) -> TaskStatus:
    task_id = await TasksRepository.add_one(task)
    return { "added": True, "task_id": task_id}


@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TasksRepository.get_all()
    return tasks
