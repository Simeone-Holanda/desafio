from pydantic import BaseModel

class Tag(BaseModel):
    id : str
    name : str
