from sqlalchemy.orm import Session
from app.models.database_init import User
from app.schemas.validation import User as PydanticUser


def create_user(user_data: PydanticUser, session: Session):
    validated_data = user_data.model_dump()
    
    new_user = User(**validated_data)
    
    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return new_user


def get_user(user_id: str, session: Session):
    return session.query(User).filter(User.id == user_id).first()


def update_username(username: str, user_id: str, session: Session):
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        user.username = username
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    return "User not found"


def get_channel_id(user_id: str, session: Session):
    (channel_id,) = session.query(User.channel_id).filter(User.id == user_id).first()
    return channel_id


def update_channel_id(channel_id: str, user_id: str, session: Session):
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        user.channel_id = channel_id
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    return "User not found"