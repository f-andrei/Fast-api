from sqlalchemy.orm import Session
from app.models.database_init import Note
from app.schemas.validation import Note as PydanticNote


def create_note(session: Session, note_data: PydanticNote): # type: ignore
    validated_data = note_data.model_dump()

    new_note = Note(**validated_data)

    session.add(new_note)
    session.commit()
    session.refresh(new_note)

    return new_note

def get_note(session: Session, note_id: int): # type: ignore
    return session.query(Note).filter(Note.id == note_id).first()

def get_all_notes(session: Session, user_id: int): # type: ignore
    return session.query(Note).filter(Note.user_id == user_id).all()

def update_note(session: Session, note_id: int, note_data: PydanticNote): # type: ignore
    note = session.query(Note).filter(Note.id == note_id).first()
    if note:
        for field, value in note_data.items():
            setattr(note, field, value)
        session.commit()
        session.refresh(note)
        return note
    return None

def delete_note(session: Session, note_id: int): # type: ignore
    note = session.query(Note).filter(Note.id == note_id).first()
    if note:
        session.delete(note)
        session.commit()
        return True
    return False

