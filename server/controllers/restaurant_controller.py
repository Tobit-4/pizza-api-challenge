from flask import jsonify,make_response,Blueprint
from server.models.restaurant import Restaurant
from server.extensions import db


bp = Blueprint('restaurant', __name__, url_prefix='/restaurants')
# Getting all restaurants
@bp.route('/',methods=['GET'])
def restaurants():
    restaurants = Restaurant.query.all()
    restaurants_dict = [restaurants.to_dict() for restaurants in restaurants]

    response = make_response(jsonify(restaurants_dict),200)
    return response
# Getting a single restaurant
@bp.route('/<int:id>',methods=["GET"])
def restaurant_by_id(id):
    restaurant = Restaurant.query.get(id)

    if restaurant is None:
        return make_response(jsonify({"error":"Restaurant not found"}),404)
    return make_response(jsonify(restaurant.to_dict())), 200 

# Deleting a retaurant  
@bp.route('/<int:id>',methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return make_response(jsonify({"error": "Restaurant not found"}), 404)
    
    db.session.delete(restaurant)
    db.session.commit()
    return make_response('', 204)

