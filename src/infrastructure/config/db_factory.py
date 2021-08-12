from pymongo import MongoClient

class Database:    
    db = None

    @classmethod
    def set_connection(cls):
        """
        Creating database connection.
        """
        try:
            print("===========creted connection=============")
            client_connection = MongoClient("mongodb://127.0.0.1:27017/")
            cls.db = client_connection['db_desafio']
        except Exception as ex:
            raise ex

    @classmethod
    def get_connection(cls):
        """
        Get database connection.
        """
        print("==============Get connection=============")
        return cls.db