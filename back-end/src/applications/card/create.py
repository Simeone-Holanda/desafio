from typing import List
from datetime import datetime
from src.domains.card import Card
from src.domains.tag.tag import Tag
from src.applications.tag import CreateTag
from src.interfaces.card import CreateCardInterface
from src.infrastructure.repositories.tag_repository import TagRepository
from src.infrastructure.repositories.card_repository import CardRepository


class CreateCard:

    @classmethod
    def generate_list_tags(cls, tags) -> List[Tag]:
        """ Percorre todas a lista de tags, verifica se existe caso exista obtém essa tag do database
            caso não cria uma nova tag. """
        list_tags = []
        for tag in tags:
            if TagRepository().check_tag_exist(tag.name):
                tag = TagRepository().get_tag_by_name(tag.name)
                tag = TagRepository().obj(tag)
                list_tags.append(tag)
            else:
                list_tags.append(CreateTag.run(tag))
        return list_tags

    @classmethod
    def run(cls, data: CreateCardInterface) -> Card:
        """ Prepara os dados para o formato permitido e então salva."""
        list_tags = cls.generate_list_tags(data.tags)
        card = Card(id=Card.generate_id(),
                    text=data.text,
                    data_criacao=datetime.now(),
                    data_modificacao=datetime.now(),
                    tags=list_tags)
        CardRepository().save(card.dict())
        return card
