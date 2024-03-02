from sqlalchemy.orm import Session
from app.models.database_init import Task
from app.schemas.validation import Task as PydanticTask


def create_task(session: Session, task_data: PydanticTask): # type: ignore
    validated_data = task_data.model_dump()

    new_task = Task(**validated_data)

    session.add(new_task)
    session.commit()
    session.refresh(new_task)

    return new_task

def get_task(session: Session, task_id: int): # type: ignore
    return session.query(Task).filter(Task.id == task_id).first()

def get_all_tasks(session: Session, user_id: str): # type: ignore
    return session.query(Task).filter(Task.user_id == user_id).all()

def update_task(session: Session, task_id: int, task_data: PydanticTask): # type: ignore
    task = session.query(Task).filter(Task.id == task_id).first()
    if task:
        # Update only the provided fields
        for field, value in task_data.items():
            setattr(task, field, value)
        session.commit()
        session.refresh(task)
        return task
    return None

def delete_task(session: Session, task_id: int): # type: ignore
    task = session.query(Task).filter(Task.id == task_id).first()
    if task:
        session.delete(task)
        session.commit()
        return True
    return False

