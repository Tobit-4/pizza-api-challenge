from server.extensions import db
from sqlalchemy_serializer import SerializerMixin


class Restaurant(db.Model,SerializerMixin):
    __tablename__ = 'restaurants'

    serialize_rules = ('-restaurant_pizzas.pizza', '-restaurant_pizzas.restaurant')
    id = db.Column(db.Integer(),primary_key = True)
    name = db.Column(db.String(),nullable = False)
    address = db.Column(db.String(),nullable = False)

    # Relationships
    restaurant_pizzas = db.relationship('RestaurantPizza',back_populates = 'restaurant')