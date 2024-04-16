import json
from flask import Flask
from flask_smorest import Api
import os

def create_app():
    app = Flask(__name__)

    # Load configuration from JSON file
    with open(f'{os.path.dirname(__file__)}/configuration/development.json', 'r') as config_file:
        config_data = json.load(config_file)

    app.config.update(config_data)

    from .views.items import blp as ItemBluePrint
    from .views.store import blp as StoreBluePrint

    api = Api(app)

    # Register Blueprints
    api.register_blueprint(ItemBluePrint)
    api.register_blueprint(StoreBluePrint)

    return app
