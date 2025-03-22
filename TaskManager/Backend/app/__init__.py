from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from flask_cors import CORS
import psycopg2
import os 
from dotenv import load_dotenv
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    get_jwt_identity,
    jwt_required
)

def create_app():
    app = Flask("__main__")
    load_dotenv('../../.env')

    app.config["JWT_SECRET_KEY"] = os.getenv('JWT_SECRET_KEY')

    bcrypt = Bcrypt(app)
    CORS(app)
    jwt = JWTManager(app)
        
    return app 