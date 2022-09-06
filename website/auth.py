from flask import Blueprint,render_template,request,flash,redirect,url_for
from .models import User
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user,logout_user,current_user,login_required
from . import db

auth=Blueprint('auth',__name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        user_email=request.form.get('email')
        user_pwd=request.form.get('password')
        user=User.query.filter_by(email=user_email).first()
        if user:
            if check_password_hash(user.password,user_pwd):
                flash('Logged in Successfully!',category='success')
                login_user(user,remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password!',category='error')
        else:
            flash('E-mail does not exist',category='error')
    return render_template("Login.html",user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/SignUp',methods=['GET','POST'])
def SignUp():
    if request.method=='POST':
        user_email=request.form.get('email')
        user_first_name=request.form.get('firstname')
        user_passwd_1=request.form.get('password1')
        user_passwd_2=request.form.get('password2')

        user=User.query.filter_by(email=user_email).first()
        if user:
            flash('Useer already Exists.Please Login!',category='error')
        else:
            if len(user_email)<4:
                flash("Enter valid mail with more than 4 characters",category='error')
            elif len(user_first_name)<2:
                flash("Enter First Name which is valid having more than 2 Characters",category='error')
            elif user_passwd_1!=user_passwd_2:
                flash("Passwords Not matching!!! Enter the passwords again",category='error')
            elif len(user_passwd_1)<8:
                flash("Enter password having more than 8 Characters",category='error')
            else:
                #Add user data to database
                new_user=User(email=user_email,firstName=user_first_name,password=generate_password_hash(user_passwd_1,method='sha256'))
                db.session.add(new_user)
                db.session.commit()
                flash("Account Created",category='success')
                login_user(new_user,remember=True)
                return redirect(url_for('views.home'))
    return render_template("SignUp.html",user=current_user)
