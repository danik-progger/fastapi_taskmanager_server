from pydantic import BaseModel
from typing import Optional


class Task(BaseModel):
    name: str
    description: Optional[str] = None


class STask(Task):
    id: int
    
class TaskStatus(BaseModel):
    added: bool = True
    task_id: int