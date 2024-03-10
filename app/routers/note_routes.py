from fastapi import HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session as DBSession
from app.models.database_init import Session as NoteSession
from app.schemas.validation import Note
from app.repos.note_crud import create_note, get_all_notes, get_note, update_note, delete_note


note_router = APIRouter()


def get_db():
    db = NoteSession()
    try:
        yield db
    finally:
        db.close()


@note_router.post("/note/create_note")
def create_note_endpoint(note_data: Note, db: DBSession=Depends(get_db)):
    try:
        return create_note(note_data=note_data, session=db)
    except Exception as e:
        print(e)

        db.rollback()
        raise HTTPException(status_code=500, detail="Internal Server Error")


@note_router.get("/note/get_note/{note_id}")
def get_note_endpoint(note_id: int, db: DBSession=Depends(get_db)):
    try:
        return get_note(note_id=note_id, session=db)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")


@note_router.get("/note/get_all_notes/{user_id}")
def get_note_endpoint(user_id: str, db: DBSession=Depends(get_db)):
    try:
        return get_all_notes(user_id=user_id, session=db)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")


@note_router.put("/note/update_note/{note_id}")
def update_note_endpoint(note_data: dict, note_id: int,  db: DBSession=Depends(get_db)):
    try:
        updated_note = update_note(note_data=note_data, note_id=note_id, session=db)
        if updated_note:
            return {"message": "Note updated successfully", "updated_note": updated_note}
        else:
            raise HTTPException(status_code=404, detail="Note not found")
    except Exception as e:
        print(e)
  
        db.rollback()
        raise HTTPException(status_code=500, detail="Internal Server Error")
    

@note_router.delete("/note/delete_note/{note_id}")
def delete_note_endpoint(note_id: int, db: DBSession=Depends(get_db)):
    try:
        return delete_note(note_id=note_id, session=db)
    except Exception as e:
        print(e)
        db.rollback()
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
    