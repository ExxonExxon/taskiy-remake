from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    from app.routes.auth import auth_bp
    app.register_blueprint(auth_bp)
    
    from app.routes.pages import pages_bp
    app.register_blueprint(pages_bp)
    
    from app.routes.home import home_bp
    app.register_blueprint(home_bp)

    with app.app_context():
        db.create_all()  # Create database tables

    return app
