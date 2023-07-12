from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login_view')
def login():
    return "<p> Login </p>"

@auth.route('/logout_view')
def logout():
    return "<p> logout </p>"

@auth.route('/sign-up_view')
def sign_up():
    return "<p> sign Up </p>"