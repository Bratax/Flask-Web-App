from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login_view', methods=['GET', 'POST'])
def login():
    return render_template("login.html", boolean=True)

@auth.route('/logout_view')
def logout():
    return "<p> logout </p>"

@auth.route('/sign-up_view', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
    if len (email) < 4:
        flash("email must be greater than 4 characters", category='error')
    elif len(firstName) < 2:
        flash("password must be greater than 2 characters", category='error')
    elif password1 != password2:
        flash('Password didnt match', category='error')
    elif len(password1) < 7:
        flash('password must be atleats 7 characters', category='error')
    else:
        flash('Account Created!', category='success')
        
    return render_template("sign-up.html")
