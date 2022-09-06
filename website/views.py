#In this file the standard routes is stored such as homepage about page etc..

from flask import Blueprint, flash,render_template, request,jsonify
#We are going the define this file to contain the Blueprint of our website i.e it is going to have a bunch
#bunch of URL's
import json
from flask_login import current_user,login_required
from .models import Note
from . import db
views=Blueprint('views',__name__)

@views.route('/',methods=['POST','GET'])
@login_required
def home():
    #return "<h1> Hellooooooooo</h1>"
    #Once we define our templates what we have to do is render the template by using render_template
    if request.method=='POST':
        note=request.form.get('note')
        if len(note)<1:
            flash('Enter a note',category='error')
        else:
            new_note=Note(Text_user=note,user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Added Note',category='success')
    return render_template("home.html",user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})