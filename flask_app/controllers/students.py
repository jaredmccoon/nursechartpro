from flask import render_template, redirect, request, session
from flask_app import app, bcrypt
from flask_app.models.course import Course
from flask_app.models.student import Student
from flask_app.models.submission import Submission

@app.route('/student/<int:id>')
def student(id):
    return render_template('student.html')

@app.route('/new_submission')
def submission():
    submissions = Submission.get_all_by_student({'student_id':session['studentid']})
    return render_template('student_view.html', submissions=submissions)

@app.route('/submit/<int:id>')
def completed(id):
    Submission.student_submission(id)
    return redirect('/student/{}')