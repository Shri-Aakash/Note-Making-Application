from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager 
##Initialize Database
db=SQLAlchemy()
DB_NAME="UserInfo.db"

def create_app():
    app=Flask(__name__)
    #app.config['SESSION_TYPE']='memchached'
    #app.config['SECRET KEY']='12345'
    #The above line encrypts the session data and cookies used by the website
    app.config['SQLALCHEMY_DATABASE_URI']=f'sqlite:///{DB_NAME}'
    db.init_app(app)
    #Once we write the routes for the webpage and here's where they are
    from .views import views
    from .auth import auth
    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')
    #The url prefix is so that when we want  to access a particular route from a blueprint if we dont add
    #the required prefix then it will throw an error that URL not found
    #Eg: assume URL prefix for auth is '/auth/' but on the link 127.0.0.1:5000 we just enter /login.
    #This will throw an error, and the correct path would be 127.0.0.1:5000/auth/login

    from .models import User,Note
    Create_DB(app)
    login_manager=LoginManager()
    login_manager.login_view='auth.login'
    login_manager.init_app(app)
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    return app

def Create_DB(app):
    if not path.exists('website/'+DB_NAME):
        db.create_all(app=app)
        print('Created Database!')