from flask import Flask

from config import Config


app = Flask(__name__)
app.config.from_object(Config)

from app.db import db

db.init_app(app)


from notes import notes_blueprint

app.register_blueprint(
    notes_blueprint,
    url_prefix="/notes",
)

from app.routes import *
