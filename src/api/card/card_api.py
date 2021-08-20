from src.util import JSONPayload
from flask import Blueprint, jsonify , abort
from src.interfaces.tag import CreateTagInterface
from werkzeug.exceptions import BadRequest, NotFound
from src.interfaces.card import CreateCardInterface, UpdateCardInterface
from src.applications.card import ReadCard, CreateCard, UpdateCard, ListByTag, DeleteCard

CardAPI = Blueprint('card_api',__name__)


@CardAPI.route('/cards/', methods=['GET'])
def get_all_cards():
    """ Retorna todos os cards presentes no database"""
    try:
        data = ReadCard().run()
    except Exception as ex:
        print(ex)
        return jsonify({'code': '500','message':'Internal server error'})
    else:
        return jsonify({'code': '200','data': data})


@CardAPI.route('/card/',methods=['POST'])
def create_card():
    """ Cria um card com base nos dados passado no body da requisição """
    try:
        data_card = JSONPayload(CreateCardInterface)
        card = CreateCard().run(data_card)
    except BadRequest as ex:
        return jsonify({'code': '400','message':str(ex)})
    except Exception as ex:
        print(ex)
        return jsonify({'code': '500','message':'Internal server error'})
    else:
        return jsonify({'code':'200','message':'Created card with sucess.'})


@CardAPI.route('/card/<id>',methods=['POST'])
def update_card(id):
    """ Atualiza um card pelo id """
    try:
        data_card = JSONPayload(UpdateCardInterface)
        card_updated = UpdateCard().run(id, data_card)
    except NotFound as ex:
        print(ex)
        return jsonify({'code': '404','message': str(ex)})
    except BadRequest as ex:
        return jsonify({'code': '400','message': str(ex)})
    except Exception as ex:
        print(ex)
        return jsonify({'code': '500','message':'Internal server error'})
    else:
        return jsonify({'code':'200','message':'Updated card with sucess.'})


@CardAPI.route('/card/tag',methods=['POST'])
def list_card_by_tag():
    """ lista dados por uma determinada tag."""
    try:
        data_card = JSONPayload(CreateTagInterface)
        list_data = ListByTag.run(data_card)
    except NotFound as ex:
        print(ex)
        return jsonify({'code': '404','message': str(ex)})
    except BadRequest as ex:
        return jsonify({'code': '400','message':'Tag was not found in our database.'})
    except Exception as ex:
        print(ex)
        return jsonify({'code': '500','message':'Internal server error'})
    else:
        print(list_data)
        return jsonify({'code':'200','data':list_data})


@CardAPI.route('/card/delete/<id>',methods=['DELETE'])
def delete_card(id):
    """ Deleta um card por id."""
    try:
        if id == None:
            abort(400,'Id is required! ')
        DeleteCard.run(id)
    except BadRequest as ex:
        return jsonify({'code': '400','message':'Tag was not found in our database.'})
    except NotFound as ex:
        return jsonify({'code': '404','message': 'card not found'})
    except Exception as ex:
        print(type(ex))
        return jsonify({'code': '500','message':'Internal server error.'})
    else:
        return jsonify({'code':'204','message':'There is no answer for this method.'})
