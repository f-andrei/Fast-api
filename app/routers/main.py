import sys
sys.path.insert(0, 'C:\\Programming\\Python\\Sandbox\\Fast-api')

from fastapi import FastAPI
from app.routers.note_routes import note_router
from app.routers.task_routes import task_router
from app.models.database_init import Base, engine

Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(task_router)
app.include_router(note_router)