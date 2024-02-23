from flask import Blueprint


notes_blueprint = Blueprint(
    "notes",
    __name__,
    template_folder="templates",
)
"""
Создаем логический модуль
В рамках модуля с этим объектом работа происходит аналогично объекту фласк приложения 
"""

from notes.routes import *

"""
Роуты импортируем по тем же причнам что и в файле app/__init__.py
"""
