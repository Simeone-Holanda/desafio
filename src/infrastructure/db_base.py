from pydantic.main import BaseModel
from pymongo.mongo_client import MongoClient


class BaseRepository:
    _conn = None
    _collection = None
    _data_type = None
    
    def save(self, data, id = None):
        """ Cria um documento de acordo com os dados passados."""
        if id is None:
            id_data = data.pop('id')
        else:
            id_data = id
        try:
            self._conn[self._collection].update_one({'_id': id_data}, {"$set":data}, upsert=True)
        except Exception as ex:
            print(ex)
            raise Exception('Erro in the method save()')
    
    def find(self, query):
        """ retorna dados com base em uma query passada"""
        return self._conn[self._collection].find(query)

    def find_by_id(self, id: str):
        """ retorna um dado com base no id."""
        data = self._conn[self._collection].find_one({'_id':id})
        return data

    def delete_by_id(self, id: str):
        """ Deleta um dado com base no seu id"""
        return self._conn[self._collection].delete_one({'_id':id})

    def get_conn(self) -> MongoClient:
        """ Obtem a conexão junto a colections do repositorio"""
        return self._conn[self._collection]

    def obj(self, data_obj):
        """ Retorna um objeto de acordo com o data_type do repositorio"""
        data_obj['id'] = data_obj.pop('_id')
        return self._data_type(**data_obj)

    def set_conn(self, conn):
        """ Define a conexão de repositorio com o banco"""
        self._conn = conn

    def set_data_type(self, type : BaseModel):
        """ Define o tipo de dado que o repositório vai ter. 
        [NOTE] : Todos os tipos de dados definidos aqui são classes criadas com base no pydantic.
        """
        self._data_type = type

    def set_collection(self, collection):
        """ Definimos a collection para esse repositório"""
        self._collection = collection