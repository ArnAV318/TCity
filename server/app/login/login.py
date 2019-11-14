from flask import Flask,render_template, Blueprint, redirect, url_for,request
from app.forms import LoginForm,RegistrationForm
login = Blueprint('loginpage',__name__)
from app.models import user
from app import bcrypt,db,login_manager
from flask_login import login_user, current_user, logout_user, login_required

@login.route('/register' ,methods=['GET', 'POST'])
def registrationpage():
    if current_user.is_authenticated:
        return redirect(url_for('homepage.homepage'))
    form1=LoginForm()
    form2=RegistrationForm()
    if form2.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form2.password.data).decode('utf-8')
        print(form2.name.data)
        type(form2.name.data)
        u = user(form2.name.data, form2.email.data, form2.address.data,form2.password.data)
        db.session.add(u)
        db.session.commit()
        print(u)
        
        return redirect(url_for('loginpage.loginpage'))
    return render_template('register.html',form1=form1,form2=form2)

@login.route('/login' ,methods=['GET', 'POST'])
def loginpage():
    if current_user.is_authenticated:
        return redirect(url_for('homepage.homepage'))
    print('hi')
    form1=LoginForm()
    form2=RegistrationForm()
    if request.method == "POST":
        print("hii")
        print(form1)
        print(form1.email.data)
        usery = user.query.filter_by(email=form1.email.data).first()
        if usery and (usery.password== form1.password.data):
            print("true")
            login_user(usery)
            print('login successfull')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('homepage.homepage'))
    
    return render_template('login.html',form1=form1,form2=form2)

@login.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('homepage.homepage'))
