from flask import Blueprint, jsonify, request
from server.extensions import db
from server.models.pizza import Pizza
from server.models.restaurant import Restaurant
from server.models.restaurant_pizza import RestaurantPizza

bp = Blueprint('restaurant_pizza', __name__, url_prefix='/restaurant_pizzas')

@bp.route('/debug', methods=['GET'])
def debug():
    return jsonify({"message": "Connection works!"}), 200

@bp.route('/',methods=['POST'])
def create_restaurant_pizza():
    
    data = request.get_json()
    if not all(field in data for field in ['price', 'pizza_id', 'restaurant_id']):
        return jsonify({"errors": ["Missing required fields"]}), 400
    
    # Validate price range
    price = data['price']
    if not isinstance(price, int) or not 1 <= price <= 30:
        return jsonify({"errors": ["Price must be between 1 and 30"]}), 400
    
    pizza = Pizza.query.get(data['pizza_id'])
    restaurant = Restaurant.query.get(data['restaurant_id'])
    
    if not pizza or not restaurant:
        return jsonify({"error": "Pizza or Restaurant not found"}), 404
    
    try:
        # Create new RestaurantPizza
        new_rp = RestaurantPizza(
            price=price,
            pizza_id=data['pizza_id'],
            restaurant_id=data['restaurant_id']
        )
        db.session.add(new_rp)
        db.session.commit()
        
        # success response
        response = {
            "id": new_rp.id,
            "price": new_rp.price,
            "pizza_id": new_rp.pizza_id,
            "restaurant_id": new_rp.restaurant_id,
            "pizza": {
                "id": pizza.id,
                "name": pizza.name,
                "ingredients": pizza.ingredients
            },
            "restaurant": {
                "id": restaurant.id,
                "name": restaurant.name,
                "address": restaurant.address
            }
        }
        
        return jsonify(response), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"errors": [str(e)]}), 400