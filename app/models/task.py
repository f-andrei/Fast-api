from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, Float, String, Date, Time
from app.settings import DATABASE_URL

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()
Base.metadata.create_all(engine)


class Task(Base):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    links = Column(String)
    start_date = Column(Date)
    time = Column(Time)
    duration = Column(Float)
    user_id = Column(Integer)

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