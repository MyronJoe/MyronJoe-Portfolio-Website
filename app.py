from flask import Flask, render_template, url_for, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '34572773a493b3a41f6a6f251dda0c73'


@app.route('/')
def home():
    return render_template('index.html', title='Home')


@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Register', form=form)


if __name__ == '__main__':
    app.run(debug=True)
