import os

from dotenv import load_dotenv
load_dotenv() # Добавляем в окружение переменные из файла .env


class Config:
    FLASK_DEBUG: bool = bool(os.getenv("FLASK_DEBUG")) # Забираем из окружения значения указанных переменных
    SQLALCHEMY_DATABASE_URI: str = os.getenv("DATABASE_URI")
