from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)


@auth.route('/signup')
def signup():
    return 'this is the sin up page'


@auth.route('/login')
def login():
    return "Log in here"


@auth.route('/logout')
def logout():
    return 'You are loggin out'
