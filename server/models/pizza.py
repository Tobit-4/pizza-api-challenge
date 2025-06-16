from server.extensions import db
from sqlalchemy_serializer import SerializerMixin


class Pizza(db.Model,SerializerMixin):
    __tablename__ = 'pizzas'

    serialize_rules = ('-restaurant_pizzas.pizza', '-restaurant_pizzas.restaurant')
    id = db.Column(db.Integer(),primary_key=True)
    name = db.Column(db.String(),nullable=False)
    ingredients = db.Column(db.String(),nullable=False)

    # Relationships
    restaurant_pizzas = db.relationship('RestaurantPizza',back_populates = 'pizza')