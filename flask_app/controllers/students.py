from flask import render_template, redirect, request, session
from flask_app import app, bcrypt
from flask_app.models.student import Student

@app.route('/student/<int:id>')
def student(id):
    return render_template('student.html')