from datetime import datetime, time
from typing import Optional, List
from pydantic import BaseModel


class Task(BaseModel):
    name: str
    description: str
    links: Optional[str] = None
    start_date: datetime
    time: time
    duration: float
    user_id: str


class RepeatDays(BaseModel):
    task_id: int
    day_number: List[int]


class Note(BaseModel):
    name: str
    description: str
    links: Optional[str] = None
    created_at: datetime
    user_id: str


class User(BaseModel):
    id: str
    username: str
    channel_id: int
    server_id: str