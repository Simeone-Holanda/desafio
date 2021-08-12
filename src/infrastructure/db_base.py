from os import abort


class BaseRepository:
    _conn = None
    _collection = None

    def create(self, data, replace = False):
        """ Cria um documento de acordo com os dados passados"""
        id = data.pop('id')
        try:
            if replace == True:
               self._conn[self._collection].replace({'_id': id},{"$set":data})
            else:
                 self._conn[self._collection].update_one({'_id': id}, {"$set":data}, upsert=True)
        except Exception as ex:
            print(ex)
            raise Exception('Erro in the method create()')
    
    def find_by_id(self, id: str):
        data = self._conn[self._collection].find_one({'_id':id})
        if data is None:
            return None
        return data

    def delete_by_id(self):
        return self._conn[self._collection].delete_one({'_id':id})

    def set_conn(self, conn):
        self._conn = conn

    def set_collection(self, collection):
        self._collection = collection