from flask import render_template, redirect, request, session
from flask_app import app, bcrypt
from flask_app.models.admin import Admin
from flask_app.models.school import School
from flask_app.models.course import Course
from flask_app.models.teacher import Teacher
from flask_app.models.student import Student


@app.route('/admin/<int:id>')
def student(id):
    admin = Admin.get_one(id)
    return render_template('admin.html', admin=admin)

@app.route('/sysadmin/<int:id>')
def studentnew():
    return render_template('sys_admin.html')

@app.route('/new_admin')
def newadmin():
    return render_template('add_admin.html')

@app.route('/new_admin/<int:id>')
def adminnew():
    return render_template('add_admin.html')

@app.route('/new_school')
def newschool():
    admins = Admin.get_all()
    return render_template('show_add_school.html',admins=admins)

@app.route('/new_course/<int:id>')
def newcourse(id):
    courses = Course.get_all_by_school(id)
    teachers = Teacher.get_all_by_school(id)
    students = Student.get_all_by_school(id)
    return render_template('show_add_course.html', courses=courses, teachers=teachers, students=students)

@app.route('/new_teacher/<int:id>')
def newteacher(id):
    return render_template('show_add_teacher.html', id=id)

@app.route('/new_student/<int:id>')
def newstudent(id):
    return render_template('show_add_student.html',id=id)

@app.route('/add_school', methods=['POST'])
def addschool():
    School.save(request.form)
    return redirect('/new_school')

@app.route('/add_course/<int:id>', methods=['POST'])
def addcourse(id):
    data = {
        **request.form,
        'school_id':id
    }
    Course.save(data)
    return redirect(f'/new_course/{id}')

@app.route('/add_teacher/<int:id>', methods=['POST'])
def addteacher(id):
    data = {
        **request.form,
        'school_id':id
    }
    Teacher.save(data)
    return redirect(f'/new_teacher/{id}')

@app.route('/add_student/<int:id>', methods=['POST'])
def addstudent(id):
    data = {
        **request.form,
        'school_id':id
    }
    Student.save(data)
    return redirect(f'/new_student/{id}')

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