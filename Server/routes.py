from flask import render_template, request, redirect, flash, url_for
from Server import app
import json
from Server.script import checkLogin, createNewUser
import uuid

secret_key = str(uuid.uuid4()).upper()
secret_key = secret_key.replace("-", "")
app.config['SECRET_KEY'] = secret_key[0:32]

user = "admin@admin.com"
password = "password"


@app.route('/home')
def home():
    return render_template('MainPage.html')


@app.route('/', methods=['GET'])
def login():
    return render_template('login.html', form=request.form)


@app.route('/', methods=['POST'])
def login_Post():
    validation = checkLogin(request.form['inputEmail'], request.form['inputPassword'])
    if validation:
        return redirect(url_for('home'))
    flash(u'Wrong credentials', category="error")
    return render_template('login.html', form=request.form)


@app.route('/book')
def book():
    return render_template('Book.html')

@app.route('/book', methods=['POST'])
def addFavourite():
    users = request.get_json()
    user_id = users.get('username')
    items = request.get_json()
    item_id = items.get('title')
    with open('favourites.json', 'r') as f:
        favourites = json.load()

    if not favourites.get(user_id):
        favourites[user_id] = []

    favourites.append(item_id)
    with open('favourites.json', 'w') as f:
        json.dump(favourites, f)
        flash(u'Added to Favourites!', category="info")



@app.route('/foreign')
def foreign():
    return render_template('Foreign.html')


@app.route('/profile')
def profile():
    return render_template('Profile.html')


@app.route('/shopping-cart')
def shoppingCart():
    return render_template('ShoppingCart.html')


@app.route('/sign-up', methods=['GET'])
def signUp():
    return render_template('Signup.html')

@app.route('/sign-up', methods=['POST'])
def signup_Post():
    if request.form['password'] == request.form['repeatPassword']:
        createNewUser(request.form['name'], request.form['surname'], request.form['username'],
                      request.form['inputEmail'], request.form['password'])

        flash('User registered successfully!  Please log in.', category="usercreated")
        return redirect(url_for('login'))
    flash('Password do not match')
    return render_template('Signup.html', form=request.form)
