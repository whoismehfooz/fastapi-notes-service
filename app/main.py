from fastapi import FastAPI , status , Request , HTTPException
from app.mock_data import notes
from app.schemas import NoteCreate




app = FastAPI()

@app.post('/notes', status_code = status.HTTP_201_CREATED)
async def create_note(note:NoteCreate):
    new_note = note.model_dump()

    new_note['id'] = len(notes) + 1

    notes.append(new_note)

    return {'Status':'Note created successfully...',
    'data':new_note}



@app.get('/notes',status_code=status.HTTP_200_OK)
async def get_notes():
    return {'data':notes}

@app.get('/notes/{note_id}',status_code=status.HTTP_200_OK)
async def get_notes(note_id:int):
    for one_note in notes:
        if one_note['id'] == note_id:
            return {'data':one_note}
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="NOT FOUND!"
    )


@app.put('/notes/{note_id}',status_code=status.HTTP_201_CREATED)
async def update_note(note_id:int,note:NoteCreate):
    for one_note in notes:
        if one_note['id'] == note_id:
            one_note['title'] = note.title
            one_note['content'] = note.content

            return {
                'message':'note UPDATED successfully....',
                "data":one_note}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='no NOTE found for this ID.... '
    )


@app.delete('/notes/{notes_id}',status_code=status.HTTP_200_OK)
async def delete_note(notes_id:int,note:NoteCreate):
    for index, one_note in enumerate(notes):
        if one_note['id'] == notes_id:
            deleted_note = notes.pop(index)
            return {
                'msg':'note DELETED successfully...',
                'deleted_note':deleted_note
                }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        details='no NOTE found for this ID......'
    )