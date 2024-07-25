from urllib import request

from flask import Flask, request

from flask_migrate import  Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select
from blueprints import api_bp



from veri import *


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://e_ticaret_user:kamil6111@localhost:5432/e_ticaret'


    db.init_app(app)
    migrate = Migrate()
    migrate.init_app(app, db)

    @app.route('/')
    def index():
        return {"Sunucu": "eTicaret"}


    app.register_blueprint(api_bp, url_prefix='/api')


    return app