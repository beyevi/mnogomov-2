"""
Main module for Mnogomov app
"""

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
import os

TEMPLATE_DIR = os.path.abspath('./templates')
STATIC_DIR = os.path.abspath('./static')


app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mnogomov.db'
db = SQLAlchemy(app)

# @app.route('/')
# def display_welcome():
#     """
#     Display application welcome page
#     """
#     return render_template('welcome.html')


@app.route('/')
@app.route('/mainpage')
def display_mainpage():
    """
    Display application main page
    """
    return render_template('main.html')


# @app.route('/practice')
# def display_practice():
#     """
#     Display application practice page
#     """
#     return render_template('practice.html')


@app.route('/dictionary')
def display_dictpage():
    """
    Display application dictionary page
    """
    return render_template('dictionary.html')


@app.route('/profile')
def display_user_profile():
    """
    Display user profile page
    """
    return render_template('profile.html')


# @app.route('/about')
# def display_about():
#     """
#     Display application about page
#     """
#     return render_template('about.html')


@app.route('/lesson')
def display_lesson():
    """
    Display lesson
    """
    return render_template('lesson.html')


if __name__ == '__main__':
    app.run(debug=True)
