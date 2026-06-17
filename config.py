import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'agenda_facil_secret_key_2026'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///agenda_facil.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
