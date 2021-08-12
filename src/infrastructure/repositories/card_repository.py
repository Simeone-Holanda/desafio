from src.infrastructure.db_base import BaseRepository
from src.infrastructure.config import Database

class CardRepository(BaseRepository):

    def __init__(self) -> None:
        Database.set_connection()
        super().set_conn(Database.get_connection())
        super().set_collection('Cards')
