from app import db, login_manager
from flask_login import UserMixin # This class allows you to work with the user

@login_manager.user_loader
def load_user(user_id):
    # This line will send a query to the DB to search for a specific user by his ID
    return User.query.get(int(user_id))

# In brackets we indicate the model in order to create a database later
class User(db.Model, UserMixin):
    # In brackets we describe the table fields
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(40), nullable=False)

    def __repr__(self):
        # This method determines how the model object will look as a string
        return f'<User {self.username}, email: {self.emai}>'
