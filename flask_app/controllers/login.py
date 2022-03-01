from flask import render_template, redirect, request, session
from flask_app import app, bcrypt
from flask_app.models.admin import Admin
from flask_app.models.teacher import Teacher
from flask_app.models.student import Student

@app.route('/')
def login():
    if 'admin' in session:
        return redirect('/admin')
    elif 'teacher' in session:
        return redirect('/teacher')
    elif  'student' in session:
        return redirect('/student')
    return render_template('login.html')

@app.route('/admin/login')
def adminlogin():
    is_valid = Admin.validator_login(request.form)

    if not is_valid:
        return redirect('/')
    return redirect

@app.route('/teacher/login')
def teacherlogin():
    is_valid = Teacher.validator_login(request.form)

    if not is_valid:
        return redirect('/')
    return redirect

@app.route('/student/login')
def studentlogin():

    is_valid = Student.validator_login(request.form)

    if not is_valid:
        return redirect('/')
    return redirect