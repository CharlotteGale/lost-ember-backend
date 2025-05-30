from flask import Flask
from app.config.db_config import init_db
from app.models.player import Player
from app.routes.character import character_bp

app.register_blueprint(character_bp)

def create_app():
    app = Flask(__name__)
    init_db(app)

    return app