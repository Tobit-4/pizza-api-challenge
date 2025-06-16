from flask import jsonify,make_response,Blueprint
from server.models.pizza import Pizza
from server.extensions import db


bp = Blueprint('pizza', __name__, url_prefix='/pizzas')

# getting all pizzas
@bp.route('/',methods=['GET'])
def get_all_pizzas():
    pizzas = Pizza.query.all()
    pizza_to_dict = [pizza.to_dict() for pizza in pizzas]

    return make_response(jsonify(pizza_to_dict),200)