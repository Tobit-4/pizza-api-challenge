from flask import Flask
from server.extensions import db, migrate

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://pizza_user:fidel123@localhost:5432/pizza_restaurant'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    
    with app.app_context():
       
        from server.models.pizza import Pizza
        from server.models.restaurant import Restaurant
        from server.models.restaurant_pizza import RestaurantPizza
        
        # register blueprints
        from server.controllers.pizza_controller import bp as pizza_bp
        from server.controllers.restaurant_controller import bp as restaurant_bp
        from server.controllers.restaurant_pizza_controller import bp as rp_bp
        
        app.register_blueprint(pizza_bp)
        app.register_blueprint(restaurant_bp)
        app.register_blueprint(rp_bp)
    
    return app
app = create_app()

@app.route('/')
def home():
    return 'Index for Restaurant/pizza/RestaurantPizzas'
if __name__ == '__main__':
    app.run(port=5555, debug=True)