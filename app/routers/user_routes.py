from typing import List
from fastapi import HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session as DBSession
from app.models.database_init import Session as TaskSession
from app.schemas.validation import User
from app.repos.user_crud import (
    create_user, get_user, update_username, update_channel_id)

user_router = APIRouter()


def get_db():
    db = TaskSession()
    try:
        yield db
    finally:
        db.close()


@user_router.post("/user/create_user")
def create_user_endpoint(user_data: User, db: DBSession=Depends(get_db)):
    try:
        return create_user(user_data=user_data, session=db)
    except Exception as e:
        print(e)
        raise HTTPException(status=500, detail="Internal Server Error")
    

@user_router.get("/user/get_user/{user_id}")
def get_user_endpoint(user_id: str, db: DBSession=Depends(get_db)):
    try:
        return get_user(user_id=user_id, session=db)
    except Exception as e:
        print(e)
        raise HTTPException(status=500, detail="Internal Server Error")
    

@user_router.put("/user/update_username/{user_id}/{username}")
def update_discord_user_endpoint(username: str, user_id: str, db: DBSession=Depends(get_db)):
    try:
        return update_username(username=username, user_id=user_id, session=db)
    except Exception as e:
        raise HTTPException(status=500, detail="Internal Server Error")
    

@user_router.put("/user/update_channel_id/{user_id}/{channel_id}")
def update_preferred_channel_endpoint(channel_id: int, user_id: str, db: DBSession=Depends(get_db)):
    try:
        return update_channel_id(channel_id=channel_id, user_id=user_id, session=db)
    except Exception as e:
        raise HTTPException(status=500, detail="Internal Server Error")
