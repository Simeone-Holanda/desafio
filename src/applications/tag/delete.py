from os import name
from src.domains.tag import Tag
from src.interfaces.tag import CreateTagInterface
from src.infrastructure.repositories.tag_repository import TagRepository

class DeleteTag:
    
    """    
    @classmethod
    def check_tag_exist(cls, tag):
        if TagRepository().check_tag_exist(tag):
            raise ValueError('Tag ja existe por favor faça outra.')"""

    @classmethod
    def run(cls, id_tag: str) -> None:
        TagRepository().delete_by_id(id_tag)
        print("Deletado!")
        # retorna um abort ou algo do tipo aqui
