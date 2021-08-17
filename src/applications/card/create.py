from datetime import datetime
from src.domains.card import Card
from src.applications.tag import CreateTag
from src.interfaces.card import CreateCardInterface
from src.infrastructure.repositories.tag_repository import TagRepository
from src.infrastructure.repositories.card_repository import CardRepository


class CreateCard:

    @classmethod
    def run(cls, data: CreateCardInterface) -> Card:
        list_tag = []
        for tag in data.tags:
            if TagRepository().check_tag_exist(tag.name):
                tag = TagRepository().get_tag_by_name(tag.name)
                tag = TagRepository().obj(tag)
                list_tag.append(tag)
            else:
                list_tag.append(CreateTag.run(tag))

        card = Card(id=Card.generate_id(),
                    text=data.text,
                    data_criacao=datetime.now(),
                    data_modificacao=datetime.now(),
                    tags=list_tag)

        CardRepository().save(card.dict())
        return card
