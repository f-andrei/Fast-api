from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, Float, String, Date, Time, DateTime
from app.settings import DATABASE_URL

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()



class Task(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    links = Column(String)
    start_date = Column(Date)
    time = Column(Time)
    duration = Column(Float)
    user_id = Column(String)

    def __repr__(self) -> str:
        return (
            f"<Task("
            f"id={self.id}, "
            f"name='{self.name}', "
            f"description='{self.description}', "
            f"links='{self.links}', "
            f"start_date='{self.start_date}', "
            f"time='{self.time}', "
            f"duration={self.duration}, "
            f"user_id={self.user_id}"
            f")>"
        )
    

class RepeatDays(Base):
    __tablename__ = "repeat_days"
    
    id = Column(Integer, primary_key=True)
    task_id = Column(Integer)
    day_number = Column(Integer)

    def __repr__(self) -> str:
        return (
            f"<RepeatDays("
            f"id={self.id}, "
            f"task_id='{self.task_id}', "
            f"day_number'{self.day_number}"
            f")>"
        )


class Note(Base):
    __tablename__ = "note"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    links = Column(String)
    created_at = Column(DateTime)
    user_id = Column(String)

    def __repr__(self) -> str:
        return (
            f"<Note("
            f"id={self.id}, "
            f"name='{self.name}', "
            f"description='{self.description}', "
            f"links='{self.links}', "
            f"created_at='{self.created_at}', "
            f"user_id={self.user_id}"
            f")>"
        )
    

class User(Base):
    __tablename__ = "user"

    id = Column(String, primary_key=True)
    username = Column(String)
    channel_id = Column(Integer)
    server_id = Column(String)

    def __repr__(self) -> str:
        return (
            f"<User("
            f"id={self.id}"
            f"username={self.username}"
            f"channel_id={self.channel_id}"
            f"server_id={self.server_id}"
            f")>"
        )