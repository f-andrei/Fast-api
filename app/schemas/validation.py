from datetime import datetime, time
from typing import Optional
from pydantic import BaseModel


class Task(BaseModel):
    name: str
    description: str
    links: Optional[str]
    start_date: datetime
    time: time
    duration: float
    user_id: str


class Note(BaseModel):
    name: str
    description: str
    links: Optional[str]
    created_at: datetime
    user_id: str
