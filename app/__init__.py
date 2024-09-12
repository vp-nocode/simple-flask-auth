from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object('config.Config')

# Creating an object to work with a database
db = SQLAlchemy(app)
# db.init_app(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
# The module will redirect the user to the route we specify (to authorization)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from app import routes
