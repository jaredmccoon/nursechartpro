from flask import render_template, redirect, request, session
from flask_app import app, bcrypt
from flask_app.controllers.students import submission
from flask_app.models.course import Course
from flask_app.models.medication import Medication
from flask_app.models.student import Student
from flask_app.models.submission import Submission
from flask_app.models.teacher import Teacher

@app.route('/teacher/<int:id>')
def student(id):
    courses=Course.get_all_by_teacher(id)
    return render_template('teacher.html',courses=courses)

@app.route('/add_submission')
def submit():
    Medication.save()
    
    students = Student.get_all_by_course({'course_id':request.form['course_id']})
    for student in students:
        data = {
        **request.form,
        'sub_date':'no submission',
        'grade':'no grade',
        'teacher_id':session['teacherid'],
        'student_id':student,
        'completed':0
    }
        Submission.save(data)