from pydantic import BaseModel
from flask import request, abort

def JSONPayload(model : BaseModel):
    requests = request.get_json()
    if requests is None:
        abort(400,'Invalid Json')
    else:
        return model.parse_obj(requests)

