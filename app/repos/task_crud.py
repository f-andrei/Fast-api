from typing import List
from sqlalchemy.orm import Session
from app.models.database_init import Task, RepeatDays
from app.schemas.validation import Task as PydanticTask


def create_task(task_data: PydanticTask, session: Session): # type: ignore
    validated_data = task_data.model_dump()

    new_task = Task(**validated_data)

    session.add(new_task)
    session.commit()
    session.refresh(new_task)

    return new_task


def get_task(task_id: int, session: Session): # type: ignore
    return session.query(Task).filter(Task.id == task_id).first()


def get_all_tasks(user_id: str, session: Session): # type: ignore
    return session.query(Task).filter(Task.user_id == user_id).all()


def update_task(task_data: PydanticTask, task_id: int, session: Session): # type: ignore
    task = session.query(Task).filter(Task.id == task_id).first()
    if task:
        # Update only the provided fields
        for field, value in task_data.items():
            setattr(task, field, value)
        session.commit()
        session.refresh(task)
        return task
    return None


def delete_task(task_id: int, session: Session): # type: ignore
    task = session.query(Task).filter(Task.id == task_id).first()
    if task:
        session.delete(task)
        session.commit()
        return True
    return False


def add_repeat_days(repeat_days: List[int], task_id: int, session: Session):
    try:
        task = session.query(Task).filter(Task.id == task_id).first()
        if not task:
            return False
        for day_number in repeat_days:
            repeat_day = RepeatDays(task_id=task_id, day_number=day_number)
            session.add(repeat_day)

        session.commit()
        return True
    except Exception as e:
        print(e)
        return False
    

def get_repeat_days(task_id: int, session: Session):
    return session.query(RepeatDays).filter(RepeatDays.task_id == task_id).all()


def get_due_tasks(user_id: str, session: Session):
    return session.query(Task).filter(user_id).all()

