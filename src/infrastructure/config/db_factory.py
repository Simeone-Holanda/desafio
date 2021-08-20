from pymongo import MongoClient

class Database:    
    db = None

    @classmethod
    def set_connection(cls):
        """
        Cria a conexção com o database.

        [NOTE] - Chamamos esse metodo apenas uma vez na inicialização do serviço, apos isso 
        sempre que for acessar o banco teremos apenas que pegar e não criar uma nova conexão.

        """
        try:
            client_connection = MongoClient("mongodb://127.0.0.1:27017/")
            cls.db = client_connection['db_desafio']
        except Exception as ex:
            print(ex)
            raise ex

    @classmethod
    def get_connection(cls):
        """
        Obtém a conexão do database.
        """
        return cls.db