from flask import Flask
from config import config
import os


# Creates our Flask application.
app = Flask(__name__)

config_name = os.getenv('FLASK_CONFIG') or 'default'

#tell flask app to read the config file and use the variables
app.config.from_object(config[config_name]) 

config[config_name].init_app(app)


from app import views, errors
