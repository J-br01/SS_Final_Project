from flask import *
from Server import app
from Server.script import *
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
    else:
        flash(u'Wrong credentials', category="error")
        return render_template('login.html', form=request.form)

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

@app.route('/sign-up', methods=['GET', 'POST'])
def signUp():
    if request.method == 'POST':
        if request.form['password'] == request.form['repeatPassword']:
            createNewUser(request.form['name'], request.form['surname'], request.form['username'],
                       request.form['inputEmail'], request.form['password'])

            flash('User registered successfully!  Please log in.', category="usercreated")
            return redirect(url_for('login'))
        else:
            flash('Password do not match')
            return render_template('Signup.html', form=request.form)
    else:
        return render_template('Signup.html')