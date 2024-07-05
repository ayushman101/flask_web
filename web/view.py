from flask import Blueprint, render_template, request, flash, redirect, jsonify
from flask_login import login_required, current_user
from .model import Note
from . import db
import json

view= Blueprint("view", __name__)

@view.route("/", methods=['POST','GET'])
@login_required
def home():

    if request.method=='POST':
        note=request.form.get('note')
        if len(note)<1:
            flash("Invalid note", category='error')
        else:
            new_note=Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note Added Successfully', category='success')
    return render_template("home.html", user=current_user)

@view.route("/delete-note",methods=['DELETE'])
def deleteNote():
    data= json.loads(request.data)
    noteId= data['noteId']
    note= Note.query.get(noteId)
    if note:
        if note.user_id==current_user.id:
            db.session.delete(note)
            db.session.commit()
    
    return jsonify({})