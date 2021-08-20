from pydantic import BaseModel
from flask import request, abort

def JSONPayload(model : BaseModel):
    """ Pega os dados passado no corpo da requisição re converte para o tipo que queremos,
        caso não esteja no formato certo ja retornamos um erro para o usuário.
    """
    requests = request.get_json()
    if requests is None:
        abort(400,'Invalid Json')
    else:
        return model.parse_obj(requests)

