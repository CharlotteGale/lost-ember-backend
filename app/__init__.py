from flask import Flask
from app.config.db_config import init_db
from app.models.player import Player

def create_app():
    app = Flask(__name__)
    init_db(app)

    return app