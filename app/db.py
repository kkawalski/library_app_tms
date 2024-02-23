from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase): # Базовый класс для моделей
  pass

db = SQLAlchemy(model_class=Base) 
# Создаем объект, с помощью которого сможем работать с нашей базой данных в любом месте проекта
