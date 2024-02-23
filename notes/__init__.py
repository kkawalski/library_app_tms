from flask import Blueprint


notes_blueprint = Blueprint(
    "notes",
    __name__,
    template_folder="templates",
)

from notes.routes import *
