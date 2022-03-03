from flask import render_template, redirect, request, session
from flask_app import app, bcrypt
from flask_app.models.admin import Admin
from flask_app.models.teacher import Teacher
from flask_app.models.student import Student
from flask_app.models.sysadmin import Sysadmin

@app.route('/')
def login():
    if 'sysadmin' in session:
        id = session['sysadmin']
        return redirect(f'/sysadmin/{id}')
    elif 'admin' in session:
        id = session['admin']
        return redirect(f'/admin/{id}')
    elif 'teacher' in session:
        id = session['teacher']
        return redirect(f'/teacher/{id}')
    elif  'student' in session:
        id = session['student']
        return redirect(f'/student/{id}')
    return render_template('login.html')


@app.route('/sysadmin/login')
def adminlogin():
    is_valid = Sysadmin.validator_login(request.form)

    if not is_valid:
        return redirect('/')
    id = Sysadmin.get_id(request.form['email'])
    session['sysadmin'] = id
    return redirect(f'/sysadmin/{id}')

@app.route('/admin/login')
def adminlogin():
    is_valid = Admin.validator_login(request.form)

    if not is_valid:
        return redirect('/')
    id = Admin.get_id(request.form['email'])
    session['admin'] = id
    return redirect(f'/admin/{id}')

@app.route('/teacher/login')
def teacherlogin():
    is_valid = Teacher.validator_login(request.form)

    if not is_valid:
        return redirect('/')
    id = Teacher.get_id(request.form['email'])
    session['teacher'] = id
    return redirect(f'/teacher/{id}')

@app.route('/student/login')
def studentlogin():

    is_valid = Student.validator_login(request.form)

    if not is_valid:
        return redirect('/')
    id = Student.get_id(request.form['email'])
    session['student'] = id
    return redirect('/student')