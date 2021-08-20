from src.util import JSONPayload
from flask import Blueprint, jsonify , abort
from werkzeug.exceptions import BadRequest, Conflict, NotFound
from src.interfaces.tag import CreateTagInterface, UpdateTagInterface
from src.applications.tag import ReadTag, CreateTag, UpdateTag, DeleteTag 


TagAPI = Blueprint('tag_api',__name__)


@TagAPI.route('/tags/', methods=['GET'])
def get_all_tags():
    """ Pega todas as tags presentes no banco de dados"""
    try:
        data = ReadTag().run()
    except Exception as ex:
        return jsonify({'code': '500','message':'Internal server error'})
    else:
        return jsonify({'code': '200','data': data})

@TagAPI.route('/tag/',methods=['POST'])
def create_tag():
    """ Cria uma tag com base em dados passados no body de uma requisição """
    try:
        data_tag = JSONPayload(CreateTagInterface)
        tag = CreateTag().run(data_tag)
    except BadRequest as ex:
        return jsonify({'code': '400','message':'Tag was not found in our database.'})
    except Conflict as msg:
        return jsonify({'code': '409','message': str(msg) })
    except Exception as ex:
        print(ex)
        return jsonify({'code': '500','message':'Internal server error'})
    else:
        return jsonify({'code':'200','message':'Created tag with sucess.'})

@TagAPI.route('/tag/<id>',methods=['POST'])
def update_tag(id):
    """ atualiza uma tag pelo id """
    try:
        data_tag = JSONPayload(UpdateTagInterface)
        UpdateTag().run(id, data_tag)
    except BadRequest as ex:
        return jsonify({'code': '400','message':'Invalide json.'})
    except NotFound as ex:
        return jsonify({'code': '404','message': 'Tag not found'})
    except Exception as ex:
        print(type(ex))
        print(ex)
        return jsonify({'code': '500','message':'Internal server error'})
    else:
        return jsonify({'code':'200','message':'Updated tag with sucess.'})

@TagAPI.route('/tag/delete/<id>',methods=['DELETE'])
def delete_tag(id):
    """ Deleta um tag por id """
    try:
        if id == None:
            abort(400,'Id is required! ')
        DeleteTag.run(id)
    except BadRequest as ex:
        return jsonify({'code': '400','message':'Invalid type id.'})
    except NotFound as ex:
        return jsonify({'code': '404','message': 'card not found'})
    except Exception as ex:
        print(type(ex))
        return jsonify({'code': '500','message':'Internal server error.'})
    else:
        return jsonify({'code':'204','message':'There is no answer for this method.'})