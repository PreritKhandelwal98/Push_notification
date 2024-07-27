from flask import Flask
from flask_pymongo import PyMongo
from flask_socketio import SocketIO
from flask_cors import CORS
from bson import ObjectId
import json

# Initialize the extensions
mongo = PyMongo()
socketio = SocketIO(cors_allowed_origins="*")

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    # Enable CORS
    CORS(app)

    # Initialize the extensions with the app
    mongo.init_app(app)
    socketio.init_app(app)

    # Register the blueprint
    from app.routes import main
    app.register_blueprint(main)

    # Set the custom JSON encoder
    class JSONEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, ObjectId):
                return str(obj)
            return super(JSONEncoder, self).default(obj)
    app.json_encoder = JSONEncoder

    return app

def get_socketio():
    return socketio
