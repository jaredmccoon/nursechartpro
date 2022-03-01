from flask import render_template, redirect, request, session
from flask_app import app, bcrypt
from flask_app.models.admin import Admin
from flask_app.models.school import School
from flask_app.models.course import Course
from flask_app.models.teacher import Teacher
from flask_app.models.student import Student

@app.route('/new_school')
def newschool(id):
    session['adminid'] = id
    schools = School.get_all(id)
    return render_template('show_add_school.html', schools=schools)

@app.route('/new_course')
def newcourse():
    return render_template('show_add_course.html')

@app.route('/new_teacher')
def newteacher():
    return render_template('show_add_teacher.html')

@app.route('/new_student')
def newstudent():
    return render_template('show_add_student.html')

@app.route('/add_school')
def addschool():
    School.save(request.form)
    return redirect('/new_school')

@app.route('/add_course')
def addcourse():
    Course.save(request.form)
    return redirect('/new_course')

@app.route('/add_teacher')
def addteacher():
    Teacher.save(request.form)
    return redirect('/new_teacher')

@app.route('/add_student')
def addstudent():
    Student.save(request.form)
    return redirect('/new_student')

