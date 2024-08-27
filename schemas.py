from typing import Optional

from pydantic import BaseModel


class Task(BaseModel):
    name: str
    description: Optional[str] = None


class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None


class STask(Task):
    id: int


class StaskId(BaseModel):
    ok: bool = True
    task_id: int
