import json
from dotenv import load_dotenv
from flask import Flask
from flask_smorest import Api
import os

def create_app():
    load_dotenv()
    app = Flask(__name__)

    env = os.getenv('FLASK_ENV')

    # Load configuration from JSON file
    with open(f'{os.path.dirname(__file__)}/configuration/{env}.json', 'r') as config_file:
        config_data = json.load(config_file)

    app.config.update(config_data)

    from .views.aboutMe import blp as aboutMeBluePrint
    from .views.collectedData import blp as collectedDataBluePrint

    api = Api(app)

    # Register Blueprints
    api.register_blueprint(aboutMeBluePrint)
    api.register_blueprint(collectedDataBluePrint)

    return app
