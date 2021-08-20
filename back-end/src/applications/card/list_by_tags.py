from werkzeug.exceptions import abort
from src.domains.card import Card
from src.domains.tag import Tag
from src.infrastructure.repositories.tag_repository import TagRepository
from src.infrastructure.repositories.card_repository import CardRepository

class ListByTag:

    @classmethod
    def check_tag_exist(cls, tag_name : str):
        if not TagRepository().check_tag_exist(tag_name):
            return abort(404, 'Not found tag')

    @classmethod 
    def run(cls, tag: Tag) -> Card:
        cls.check_tag_exist(tag.name)
        return CardRepository().list_by_tag(tag.dict())
