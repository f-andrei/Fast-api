from typing import List
from fastapi import HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session as DBSession
from app.models.database_init import Session as TaskSession
from app.schemas.validation import Task
from app.settings import time_range
from app.repos.task_crud import (
    create_task, get_all_tasks, get_task, update_task, 
    delete_task, add_repeat_days, get_repeat_days, get_due_tasks)


task_router = APIRouter()


def get_db():
    db = TaskSession()
    try:
        yield db
    finally:
        db.close()


@task_router.post("/task/create_task")
def create_task_endpoint(task_data: Task, db: DBSession=Depends(get_db)):
    try:
        return create_task(task_data=task_data, session=db)
    except Exception as e:
        print(e)

        db.rollback()
        raise HTTPException(status_code=500, detail="Internal Server Error")


@task_router.get("/task/get_task/{task_id}")
def get_task_endpoint(task_id: int, db: DBSession=Depends(get_db)):
    try:
        return get_task(task_id=task_id, session=db)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")
    

@task_router.get("/task/get_all_tasks/{user_id}")
def get_task_endpoint(user_id: str, db: DBSession=Depends(get_db)):
    try:
        return get_all_tasks(user_id=user_id, session=db)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")


@task_router.put("/task/update_task/{task_id}")
def update_task_endpoint(task_data: dict, task_id: int, db: DBSession=Depends(get_db)):
    try:
        updated_task = update_task(task_data=task_data, task_id=task_id, session=db)
        if updated_task:
            return {"message": "Task updated successfully", "updated_task": updated_task}
        else:
            raise HTTPException(status_code=404, detail="Task not found")
    except Exception as e:
        print(e)
        db.rollback()
        raise HTTPException(status_code=500, detail="Internal Server Error")


@task_router.delete("/task/delete_task/{task_id}")
def delete_task_endpoint(task_id: int, db: DBSession=Depends(get_db)):
    try:
        return delete_task(task_id=task_id, session=db)
    except Exception as e:
        print(e)
        db.rollback()
        raise HTTPException(status_code=500, detail="Internal Server Error")
    

@task_router.post("/task/add_repeat_days/{task_id}")
def add_repeat_days_endpoint(repeat_days: List[int], task_id: int, db: DBSession=Depends(get_db)):
    try: 
        return add_repeat_days(repeat_days=repeat_days, task_id=task_id, session=db)
    except Exception as e:
        print(e)
        db.rollback()
        raise HTTPException(status_code=500, detail="Internal Server Error")
    

@task_router.get("/task/get_repeat_days/{task_id}")
def get_repeat_days_endpoint(task_id: int, db: DBSession=Depends(get_db)):
    try:
        return get_repeat_days(task_id=task_id, session=db)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")
        

@task_router.get("/task/get_due_tasks")
def get_due_tasks_endpoint(db: DBSession=Depends(get_db)):
    try:
        start_time_range, end_time_range = time_range()
        return get_due_tasks(start_time=start_time_range, end_time=end_time_range, session=db)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")
    