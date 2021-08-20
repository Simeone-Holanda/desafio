from os import name

from werkzeug.exceptions import abort
from src.infrastructure.repositories.tag_repository import TagRepository

class DeleteTag:
    
    @classmethod
    def check_tag_exist(cls, tag_id):
        """ Chama o metodo check_tag_exist() para verificar se a tag existe
        caso não exista é retornado um erro 404."""
        tag = TagRepository().find_by_id(tag_id)
        if tag is None:
            return abort(404,'Not found tag')

    @classmethod
    def run(cls, id_tag: str) -> None:
        """ Verifica se a tag passada existe caso exista ele é deletada.
        :param
            id_tag - id da tag.
        """
        cls.check_tag_exist(id_tag)
        TagRepository().delete_by_id(id_tag)
