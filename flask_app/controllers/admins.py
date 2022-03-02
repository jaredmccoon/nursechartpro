from flask import render_template, redirect, request, session
from flask_app import app, bcrypt
from flask_app.models.admin import Admin
from flask_app.models.school import School
from flask_app.models.course import Course
from flask_app.models.teacher import Teacher
from flask_app.models.student import Student


@app.route('/new_admin')
def newadmin():
    return render_template('add_admin.html')

@app.route('/new_admin/<int:id>')
def newadmin():
    return render_template('add_admin.html')

@app.route('/new_school/<int:id>')
def newschool(id):
    session['admin'] = id
    # schools = School.get_one(id)
    return render_template('show_add_school.html')

@app.route('/new_course')
def newcourse():
    return render_template('show_add_course.html')

@app.route('/new_teacher')
def newteacher():
    return render_template('show_add_teacher.html')

@app.route('/new_student')
def newstudent():
    return render_template('show_add_student.html')

@app.route('/add_school/<int:id>', methods=['POST'])
def addschool(id):
    data = {
        **request.form,
        'admin_id':id
    }
    School.save(data)
    return redirect(f'/new_school/{id}')

@app.route('/add_course/<int:id>/<int:id>', methods=['POST'])
def addcourse():
    session['admin'] = id
    data = {
        **request.form,
        'admin_id':id
    }
    Course.save(request.form)
    return redirect('/new_course')

@app.route('/add_teacher', methods=['POST'])
def addteacher():
    Teacher.save(request.form)
    return redirect('/new_teacher')

@app.route('/add_student', methods=['POST'])
def addstudent():
    Student.save(request.form)
    return redirect('/new_student')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/register/admin', methods=['POST'])
def adminregister():
    is_valid = Admin.validator(request.form)

    if is_valid == False:
        return redirect('/add_admin')
    
    hash_pw = bcrypt.generate_password_hash(request.form['password'])

    data = {
        **request.form,
        'password': hash_pw
    }

    id = Admin.save(data)
    session['admin'] = id
    return redirect(f'/add_admin/{id}')