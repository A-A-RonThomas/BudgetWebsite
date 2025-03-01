from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

load_dotenv()


db = SQLAlchemy()

class Config:
    DEBUG = True
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))  # Path to the folder where Flask app resides
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}"  # Database file in the same directory
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BACKEND_HOST = os.getenv("BACKEND_HOST")
    BACKEND_PORT = os.getenv("BACKEND_PORT")
    SECRET_KEY = os.getenv("SECRET_KEY")


