from flask import Flask, render_template, url_for, redirect, flash
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '34572773a493b3a41f6a6f251dda0c73'


@app.route('/')
def home():
    return render_template('index.html', title='Home')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        form.email.data = 'myron@gmail.com'
        form.password.data = '1234'
        flash('Login Successful!', 'success')
        return redirect(url_for('home'))
    # else:
    #     flash('Login failed check Username and Password', 'danger')
    return render_template('login.html', title='Register', form=form)


if __name__ == '__main__':
    app.run(debug=True)
