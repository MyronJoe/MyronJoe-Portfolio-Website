from flask import render_template, url_for, redirect, flash
from app import app, db, bcrypt
from app.forms import RegistrationForm, LoginForm
from app.models import User, Post, Message


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', title='Home')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account was created successfully', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'myron@gmail.com' and form.password.data == '1234':
            flash('Login Successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login failed check Username and Password', 'danger')
    return render_template('login.html', title='Login', form=form)