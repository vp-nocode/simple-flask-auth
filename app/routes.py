# from flask import render_template, request, redirect, url_for
from app import app, db, User

# The function creates an application context, which is needed to work with the database
with app.app_context():
    # Creating a table defined in the User class
    db.create_all()

# Using the decorator, we create a route that will call the function
@app.route('/add_user')
# The function will create an object of the User class
def add_user():
    new_user = User(username='new_username')
    db.session.add(new_user) # add to session
    db.session.commit() #  Save changes to database
    return 'User added' # Display a message that the user has been added to the

@app.route('/users')
def get_users():
    users = User.query.all()
    return str(users)

'''
@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == 'POST':
    # функция request.form извлекает значение из соответствующих полей

        user_name = request.form.get('user_name')
        age = request.form.get('age')
        city = request.form.get('city')
        hobby = request.form.get('hobby')
        # создаёт условие для проверки наличия данных в полях title и content
        # if title and content:
        #    posts.append({'title': title, 'content': content})
        if user_name and age and city and hobby:
            questionnaires.append({'user_name': user_name, 'age': age, 'city': city, 'hobby': hobby})
        #использует для обновления страницы и предотвращения повторной отправки формы.
        return redirect(url_for('index'))
        # возвращает отрендеренный шаблон с переданными данными постов
    else:
        # return render_template('blog.html', posts=posts)
        return render_template('blog.html', questionnaires=questionnaires)
'''
