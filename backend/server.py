from flask import Flask, render_template
import os


app = Flask(__name__, template_folder="../frontend/templates")


@app.route('/')
def hello():
    return {'title': 'Mnogomov', 'version': 2.0, 'team': ["bevz", "arnauta"]}


@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
