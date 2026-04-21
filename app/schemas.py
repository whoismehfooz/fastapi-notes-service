from pydantic import BaseModel


class NoteCreate(BaseModel):
    
    id : int
    title : str = None
    content : str = None
