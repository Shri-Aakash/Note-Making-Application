from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
class Note(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    Text_user=db.Column(db.String(1000))
    Note_data=db.Column(db.DateTime(timezone=True),default=func.now())
    #now defining a foreign key to link user and the notes created
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))

##Class defenition for User Schema of User Information Database
class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(150),unique=True)
    password=db.Column(db.String(150))
    firstName=db.Column(db.String(150))
    #Now have a link between user and all of his notes
    notes=db.relationship('Note')

