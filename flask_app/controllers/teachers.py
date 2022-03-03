from flask import render_template, redirect, request, session
from flask_app import app, bcrypt
from flask_app.models.teacher import Teacher

@app.route('/teacher/<int:id>')
def student(id):
    return render_template('teacher.html')