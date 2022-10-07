from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = '34572773a493b3a41f6a6f251dda0c73'


@app.route('/')
def home():
    return render_template('index.html', title='Home')


@app.route('/register')
def register():
    return render_template('register.html', title='Register')


@app.route('/login')
def login():
    return render_template('login.html', title='Register')


if __name__ == '__main__':
    app.run(debug=True)
