import sys
sys.path.insert(0, 'C:\\Programming\\Python\\Sandbox\\Fast-api')

from fastapi import FastAPI
from app.routers.note_routes import note_router
from app.routers.task_routes import task_router


app = FastAPI()

app.include_router(task_router)
app.include_router(note_router)