from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', title='Home')


@app.route('/register')
def register():
    return render_template('register.html', title='Register')


if __name__ == '__main__':
    app.run(debug=True)
