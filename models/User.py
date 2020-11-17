from database.db import fetch_engine

db = fetch_engine()


class User(db.Document):
    email = db.StringField(required=True)
    password_hash = db.StringField(required=True)