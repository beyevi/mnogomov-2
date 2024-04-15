from flask import Flask, render_template
import os


TEMPLATE_DIR = os.path.abspath('../frontend/templates')
STATIC_DIR = os.path.abspath('../frontend/static')


app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)


# @app.route('/')
# def display_welcome():
#     return render_template('welcome.html')


@app.route('/')
@app.route('/mainpage')
def display_mainpage():
    return render_template('main.html')


@app.route('/dictionary')
def display_dictpage():
    return render_template('dictionary.html')


if __name__ == '__main__':
    app.run(debug=True)
