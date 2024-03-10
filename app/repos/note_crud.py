from sqlalchemy.orm import Session
from app.models.database_init import Note
from app.schemas.validation import Note as PydanticNote


def create_note(note_data: PydanticNote, session: Session): # type: ignore
    validated_data = note_data.model_dump()

    new_note = Note(**validated_data)

    session.add(new_note)
    session.commit()
    session.refresh(new_note)

    return new_note


def get_note(note_id: int, session: Session): # type: ignore
    return session.query(Note).filter(Note.id == note_id).first()


def get_all_notes(user_id: str, session: Session): # type: ignore
    return session.query(Note).filter(Note.user_id == user_id).all()


def update_note(note_data: PydanticNote, note_id: int, session: Session): # type: ignore
    note = session.query(Note).filter(Note.id == note_id).first()
    if note:
        for field, value in note_data.items():
            setattr(note, field, value)
        session.commit()
        session.refresh(note)
        return note
    return None


def delete_note(note_id: int, session: Session): # type: ignore
    note = session.query(Note).filter(Note.id == note_id).first()
    if note:
        session.delete(note)
        session.commit()
        return True
    return False

