from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from app.settings import DATABASE_URL

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()
Base.metadata.create_all(engine)


class Note(Base):
    __tablename__ = 'note'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    links = Column(String)
    created_at = Column(DateTime)
    user_id = Column(Integer)

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