from flask import abort
from src.domains.tag import Tag
from src.interfaces.tag import UpdateTagInterface
from src.infrastructure.repositories.tag_repository import TagRepository

class UpdateTag:

    @classmethod
    def check_tag_exist(cls, tag_id):
        """ Chama o metodo check_tag_exist() para verificar se a tag existe
        caso não exista é retornado um erro 404. """
        tag = TagRepository().find_by_id(tag_id)
        if tag is None:
            return abort(404,'Not found tag')

    @classmethod
    def run(cls, id_tag, new_tag: UpdateTagInterface) -> Tag:
        """ Verifica se a tag existe pelo id caso exista é atualizado"""
        cls.check_tag_exist(id_tag)
        TagRepository().save(data=new_tag.dict(), id=id_tag)
        return new_tag
