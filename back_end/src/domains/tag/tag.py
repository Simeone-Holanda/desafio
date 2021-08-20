from typing import List, Union
from pydantic import BaseModel
from secrets import token_hex

class Tag(BaseModel):
    """ Tags são opcionais em cards então foi definido valores padrões seus atributos """
    id : str = ''
    name : Union[str, List[str]] = ''

    @classmethod
    def generate_id(self):
        return token_hex(16)
