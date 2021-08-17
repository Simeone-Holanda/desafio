from typing import List
from src.domains.card import Card
from src.infrastructure.db_base import BaseRepository
from src.infrastructure.config import Database

class CardRepository(BaseRepository):

    def __init__(self) -> None:
        super().set_conn(Database.get_connection())
        super().set_collection('Cards')
        super().set_data_type(Card)

    def list_by_tag(self,tag_filter) -> List[dict]:
        """ Busca em todos os dados da collection de cards, se existe a tag
            na lista de tags do banco de dados. 
            
            return: Lista de tags no formato de dicionarios
            """
        list_data = []
        for document in self.get_conn().find({}):
            for tag in document['tags']:
                if tag_filter['name'] == tag['name']:
                    list_data.append(document)
        return list_data
