from os import name
from flask import abort
from src.domains.tag import Tag
from src.interfaces.tag import UpdateTagInterface
from src.infrastructure.repositories.tag_repository import TagRepository

class UpdateTag:

    @classmethod
    def run(cls, id_tag, new_tag: UpdateTagInterface) -> Tag:
        TagRepository().save(data=new_tag.dict(), id=id_tag)
        
        return new_tag
