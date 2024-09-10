from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)

app.config['SECRET_KEY'] = 'your_secret_secret_key'
# connect to db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# Disabling the alarm about changes to objects inside the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Creating an object to work with a database
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
# The module will redirect the user to the route we specify (to authorization)
login_manager.login_view = 'login'

from app import routes
