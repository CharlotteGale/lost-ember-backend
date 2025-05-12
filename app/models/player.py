
from datetime import datetime
from app.config.db_config import db

class Player(db.Model):
    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    origin = db.Column(db.String, nullable=False)
    lineage = db.Column(db.String, nullable=False)
    calling = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)