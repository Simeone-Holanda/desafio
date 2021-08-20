from flask import abort
from src.domains.tag import Tag
from src.interfaces.tag import CreateTagInterface
from src.infrastructure.repositories.tag_repository import TagRepository

class CreateTag:
    
    @classmethod
    def check_tag_exist(cls, tag_name):
        """ Verifica se existe uma tag com o paramentro passado
        :param
            tag_name - nome da tag 
        """
        if TagRepository().check_tag_exist(tag_name):
            return abort(409,'Information conflict - Tag already exists.')
        
    @classmethod
    def run(cls, tag: CreateTagInterface) -> Tag:
        """ Cria uma tag """
        if ' ' in tag.name:
            tag.name = tag.name.split(" ")
        new_tag = Tag(id=Tag.generate_id(),name=tag.name)
        cls.check_tag_exist(new_tag.name)
        TagRepository().save(new_tag.dict())
        return new_tag
