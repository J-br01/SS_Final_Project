from flask import *
from Server import app
from Server.script import *

user = "admin"
password = "admin"

@app.route('/home')
def home():
    return render_template('MainPage.html')

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['inputEmail'] == user and request.form['inputPassword'] == password:
            return redirect(url_for('home'))
        else:
            return redirect(url_for('login'))
    else:
        return render_template('login.html')


@app.route('/book')
def book():
    return render_template('Book.html')


@app.route('/foreign')
def foreign():
    return render_template('Foreign.html')

@app.route('/profile')
def profile():
    return render_template('Profile.html')


@app.route('/shopping-cart')
def shoppingCart():
    return render_template('ShoppingCart.html')

@app.route('/sign-up')
def signUp():
    return render_template('Signup.html')