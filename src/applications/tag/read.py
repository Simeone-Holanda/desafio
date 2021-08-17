from pydantic.utils import path_type
from src.infrastructure.repositories.tag_repository import TagRepository

class ReadTag:

    @classmethod
    def run(cls) -> None:
        tags = TagRepository().find({})
        print(tags)
        if tags is None:
            return []
        else:
            return list(tags)
