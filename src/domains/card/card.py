from typing import List, Union
from secrets import token_hex
from pydantic import BaseModel
from datetime import datetime
from src.domains.tag import Tag


class Card(BaseModel):
    id : str
    text : str
    data_criacao : datetime 
    data_modificacao : datetime
    tags : Union[List[Tag], Tag] = None

    @classmethod
    def generate_id(self):
        return token_hex(16)
