from fastapi import FastAPI , status , Request , HTTPException , APIRouter
from app.mock_data import notes
from app.schemas import NoteCreate , NoteResponse
from typing import List


router = APIRouter()


# Creating Notes.

@router.post('/notes', status_code = status.HTTP_201_CREATED, response_model=NoteResponse)
async def create_note(note:NoteCreate):
    new_note = note.model_dump()
    new_note['id'] = len(notes) + 1
    notes.append(new_note)
    return new_note



# Get all Notes.

@router.get('/notes', response_model=List[NoteResponse])
async def get_notes():
    return notes



# Get any note by it's ID.

@router.get('/notes/{note_id}', response_model=NoteResponse)
async def get_single_note(note_id:int):
    for one_note in notes:
        if one_note['id'] == note_id:
            return one_note
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="NOT FOUND!"
    )



# Update any note by it's ID.

@router.put('/notes/{note_id}', response_model=NoteResponse)
async def update_note(note_id:int,note:NoteCreate):
    for one_note in notes:
        if one_note['id'] == note_id:
            one_note['title'] = note.title
            one_note['content'] = note.content

            return one_note

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='no NOTE found for this ID.... '
    )


# Delete any note by its ID.

@router.delete('/notes/{note_id}',status_code=status.HTTP_200_OK)
async def delete_note(note_id:int,note:NoteCreate):
    for index, one_note in enumerate(notes):
        if one_note['id'] == note_id:
            deleted_note = notes.pop(index)
            return {'msg':'note DELETED successfully...',}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        details='no NOTE found for this ID......'
    )