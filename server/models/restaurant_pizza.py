from sqlalchemy.orm import validates
from server.extensions import db
from sqlalchemy_serializer import SerializerMixin



class RestaurantPizza(db.Model,SerializerMixin):

    __tablename__ = 'restaurant_pizzas'

    serialize_rules = ('-restaurant_pizzas.pizza', '-restaurant_pizzas.restaurant')
    id = db.Column(db.Integer(),primary_key=True)
    price = db.Column(db.Integer(),nullable=False)

    # FK
    restaurant_id = db.Column(db.Integer(),db.ForeignKey('restaurants.id'))
    pizza_id = db.Column(db.Integer(),db.ForeignKey('pizzas.id'))

    # relationships
    restaurant = db.relationship('Restaurant',back_populates = 'restaurant_pizzas')
    pizza = db.relationship('Pizza',back_populates = 'restaurant_pizzas')

    @validates('price')
    def validate_price(self, key, price):
        if not 1 <= price <= 30:
            raise ValueError("Price must be between 1 and 30")
        return price
    
    def __repr__(self):
        return f'<RestaurantPizza {self.id}, Price: {self.price}>'
