from pydantic import BaseModel
from secrets import token_hex

class Tag(BaseModel):
    id : str
    name : str

    @classmethod
    def generate_id(self):
        return token_hex(16)
