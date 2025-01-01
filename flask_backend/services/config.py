from flask_sqlalchemy import SQLAlchemy
import os


db = SQLAlchemy()

class Config:
    DEBUG = True
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))  # Path to the folder where Flask app resides
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}"  # Database file in the same directory
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BACKEND_HOST = "127.0.0.1"
    BACKEND_PORT = "8000"
    SECRET_KEY = "Super-Secret-Key"


