from flask import Blueprint,  render_template ,  request, flash, redirect, url_for
import re
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from .model import User

def is_valid_email(email):
    # Define the regex pattern for a valid email
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    # Use re.match to check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False



auth= Blueprint("auth", __name__)

@auth.route("/login", methods=['POST','GET'])
def login():
    if request.method=='POST':
        print(request.form)    
    return render_template('login.html')

@auth.route("/logout")
def logout():
    return "<h1>LOGOUT PAGE</h1>"

@auth.route("/sign-up",methods=['POST','GET'])
def sign_up():
    if request.method=='POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if not is_valid_email(email):
            flash('Email must be valid ', category='error')
        elif len(firstName)<3:
            flash('first name must be atleast 3 characters', category='error')
        elif len(password1)<8:
            flash('Password must be atleast 8 characters', category='error')
        elif password1!=password2:
            flash('Confirm Password not the same as Password', category='error')
        else:
            new_user=User(email=email, first_name=firstName, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account Created!', category='success')
            return redirect(url_for('view.home')) 
            #we give the name of the blueprint.function_name as url  

    return render_template('sign-up.html')