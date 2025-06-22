
from server.app import create_app
from server.extensions import db
from server.models.pizza import Pizza
from server.models.restaurant import Restaurant
from server.models.restaurant_pizza import RestaurantPizza

def seed_database():
    app = create_app()
    
    with app.app_context():
        print("🌱 Seeding database...")
        
        db.drop_all()
        db.create_all()
        
        # Create restaurants
        restaurants = [
            Restaurant(name="Pizza Palace", address="123 Main St"),
            Restaurant(name="Italian Bistro", address="456 Oak Ave"),
            Restaurant(name="Mama Mia's", address="789 Pine Rd")
        ]
        db.session.add_all(restaurants)
        
        # Create pizzas
        pizzas = [
            Pizza(name="Margherita", ingredients="Tomato sauce, Mozzarella, Basil"),
            Pizza(name="Pepperoni", ingredients="Tomato sauce, Mozzarella, Pepperoni"),
            Pizza(name="Vegetarian", ingredients="Tomato sauce, Mozzarella, Bell peppers, Mushrooms, Olives")
        ]
        db.session.add_all(pizzas)
        db.session.commit()
        
        # Create restaurant pizzas
        restaurant_pizzas = [
            RestaurantPizza(price=10, pizza_id=1, restaurant_id=1),
            RestaurantPizza(price=12, pizza_id=2, restaurant_id=1),
            RestaurantPizza(price=15, pizza_id=3, restaurant_id=2),
            RestaurantPizza(price=11, pizza_id=1, restaurant_id=3),
            RestaurantPizza(price=13, pizza_id=2, restaurant_id=2)
        ]
        db.session.add_all(restaurant_pizzas)
        db.session.commit()
        
        print("✅ Database seeded successfully!")

if __name__ == '__main__':
    seed_database()