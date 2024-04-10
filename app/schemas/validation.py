from datetime import datetime, time
from typing import Optional, List
from pydantic import BaseModel, validator


class Task(BaseModel):
    name: str
    description: str
    links: Optional[str] = None
    start_date: datetime
    time: time
    duration: float
    user_id: str

    @validator("start_date", pre=True)
    def parse_start_date(cls, value):
        return datetime.strptime(value, "%d/%m/%Y")

class RepeatDays(BaseModel):
    task_id: int
    day_number: List[int]


class Note(BaseModel):
    name: str
    description: str
    links: Optional[str] = None
    created_at: datetime
    user_id: str

    @validator("created_at", pre=True)
    def parse_created_at(cls, value):
        return datetime.strptime(value, "%d/%m/%Y %H:%M:%S")


class User(BaseModel):
    id: str
    username: str
    channel_id: int
    server_id: str