from pydantic.main import BaseModel
from typing import List
from src.domains.tag import Tag

class CreateCardInterface(BaseModel):
    text : str
    data_criacao : str # mudar para datatime no futuro
    data_modificacao : str # mudar para datatime no futuro
    tags : List[Tag] 