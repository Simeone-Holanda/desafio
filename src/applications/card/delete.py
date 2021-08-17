from werkzeug.exceptions import abort
from src.infrastructure.repositories.card_repository import CardRepository

class DeleteCard:

    @classmethod
    def check_exist_card(cls,id):
        """ Verifica se um card existe, caso não exista obtemos um erro. """
        card = CardRepository().find_by_id(id)
        if card == None:
            return abort(404,'Not found card')

    @classmethod
    def run(cls, card_id: str) -> None:
        """ Verifica e delete um card pelo id, caso ele exista."""
        cls.check_exist_card(card_id)
        CardRepository().delete_by_id(card_id)
        print('Deletado com sucesso!')
        #return  Retorna um abort aqui
