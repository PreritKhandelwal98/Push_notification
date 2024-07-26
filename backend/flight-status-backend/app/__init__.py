from flask import Flask
from app.config import Config
from app.models import mongo
from app.routes import main

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    mongo.init_app(app)

    app.register_blueprint(main)

    return app
