from src.infrastructure.repositories.tag_repository import TagRepository

class ReadTag:

    @classmethod
    def run(cls) -> None:
        """ Busca todos os dados na collection tag do database e retorna em uma lista """
        tags = TagRepository().find({})
        if tags is None:
            return []
        else:
            return list(tags)
