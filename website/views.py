from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "<h1> TEST </h1>"

@views.route('/login')
def login():
    return "<h1> Login </h1>"

@views.route('/logout')
def logout():
    return "<h1> Logout </h1>"

@views.route('/signup')
def signup():
    return "<h1> signup </h1>"