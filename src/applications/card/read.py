from src.domains.card import Card
from src.interfaces.card import CreateCardInterface
from src.infrastructure.repositories.card_repository import CardRepository

class ReadCard:

    @classmethod
    def run(cls) -> Card:
        return list(CardRepository().find({}))
        
