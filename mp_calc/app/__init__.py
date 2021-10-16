from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap 
from app.middleware import PrefixMiddleware

import platform

application = Flask(__name__)
application.config.from_object(Config)
db = SQLAlchemy(application)
migrate = Migrate(application, db)
login = LoginManager(application)
login.login_view = 'login'
bootstrap = Bootstrap(application)

# set voc=False if you run on local computer
if 'debian' in platform.platform():
    voc = True
else:
    voc = False

application.wsgi_app = PrefixMiddleware(application.wsgi_app, voc=voc)
from app import routes, models
