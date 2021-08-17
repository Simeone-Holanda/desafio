from src.infrastructure.db_base import BaseRepository
from src.infrastructure.config import Database
from src.domains.tag import Tag

class TagRepository(BaseRepository):

    def __init__(self) -> None:
        super().set_conn(Database.get_connection())
        super().set_collection('Tags')
        super().set_data_type(Tag)

    def check_tag_exist(self, data):
        """ Verifica se uma tag existe """
        tag = self.get_conn().find_one({'name':data})
        if tag is None:
            return False
        return True
    
    def get_tag_by_name(self, name):
        return self.get_conn().find_one({'name':name})
        
