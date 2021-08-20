from pydantic import BaseModel
from typing import List, Union
from src.interfaces.tag import CreateTagInterface

class CreateCardInterface(BaseModel):
    text : str
    tags : Union[List[CreateTagInterface], CreateTagInterface]