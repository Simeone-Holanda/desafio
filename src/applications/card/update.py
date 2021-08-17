from datetime import datetime
from src.domains.card import Card
from src.domains.tag import Tag
from werkzeug.exceptions import abort
from src.interfaces.card import UpdateCardInterface
from src.infrastructure.repositories.card_repository import CardRepository
from src.infrastructure.repositories.tag_repository import TagRepository

class UpdateCard:

    @classmethod
    def check_exist_card(cls,id):
        card = CardRepository().find_by_id(id)
        if card != None:
            return card
        abort(404,'Not found card')
    
    @classmethod
    def check_tags_exist(cls, tags):
        """ Verifica se existe uma tag pelo nome, caso exista retorna ela"""
        list_tags = []
        for tag in tags:
            tg = TagRepository().get_tag_by_name(tag.name)
            if tg != None:
                list_tags.append(Tag(id=tg['_id'],name=tg['name']))
            else:
                abort(404,f'Not found tag {tag}.')
        return list_tags

    @classmethod
    def run(cls,card_id : str, data: UpdateCardInterface) -> Card:
        """ Atualiza os dados de um card """
        
        card_old = cls.check_exist_card(card_id)
        obj_tags = cls.check_tags_exist(data.tags)
        new_card = Card(id=card_id,
                        text=data.text,
                        data_criacao=card_old['data_criacao'],
                        data_modificacao=datetime.now(),
                        tags=obj_tags)
        CardRepository().save(new_card.dict(),card_id)
        return new_card
