from typing import Text
from pydantic import BaseModel
from typing import List
from src.domains.tag import Tag
from secrets import token_hex

class Card(BaseModel):
    id : str
    text : str
    data_criacao : str # mudar para datatime no futuro
    data_modificacao : str # mudar para datatime no futuro
    tags : List[Tag]

    @classmethod
    def generate_id(self):
        return token_hex(16)
