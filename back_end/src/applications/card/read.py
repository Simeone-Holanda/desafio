from src.domains.card import Card
from src.infrastructure.repositories.card_repository import CardRepository

class ReadCard:

    @classmethod
    def run(cls) -> Card:
        """ Retorna uma lista com todos os cards na collection Cards."""
        return list(CardRepository().find({}))
        
