from pydantic import BaseModel

class CreateTagInterface(BaseModel):
    name : str