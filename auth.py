from flask import Blueprint, render_template, url_for, request, redirect

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST', 'GET'])
def login():
    return render_template('login.html')

@auth.route('/login-now', methods=['POST', 'GET'])
def login_post():
    # login code
    username = request.form.get('username')
    password = request.form.get('password')

    response = ''

    if username == 'admin' and password == '@admin':
        response = redirect(url_for('main.index'))
        # return render_template('login.html')
    else:
        response = redirect((url_for('main.home')))
    return response


@auth.route('/logout')
def logout():
    return 'You are loggin out'
