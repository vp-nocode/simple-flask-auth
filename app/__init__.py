from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'your_secret_secret_key'
# connect to db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
# Disabling the alarm about changes to objects inside the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Creating an object to work with a database
db = SQLAlchemy(app)

from app import routes

# In brackets we indicate the model in order to create a database later
class User(db.Model):
    # In brackets we describe the table fields
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        # This method determines how the model object will look as a string
        return f'<User {self.username}>'
