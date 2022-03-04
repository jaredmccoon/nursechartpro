from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash, session
from flask_app import bcrypt, DATABASE




class Submission:
    def __init__(self,data):
        self.id = data['id']
        self.student_id = data['student_id']
        self.teacher_id = data['teacher_id']
        self.course_id = data['course_id']
        self.sub_date = data['sub_date']
        self.grade = data['grade']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.completed = data['completed']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO submissions (sub_date,grade,course_id,teacher_id,student_id,completed) VALUES (%(sub_date)s,%(grade)s,%(course_id)s,%(teacher_id)s,%(student_id)s,%(completed)s);"
        some_id = connectToMySQL(DATABASE).query_db(query,data)
        return some_id

    @classmethod
    def student_submission(cls, data):
        query = "UPDATE submissions SET sub_date = %(sub_date)s, completed = 1, updated_at=NOW()  WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def teacher_submission(cls, data):
        query = "UPDATE submissions SET grade = %(grade)s, updated_at=NOW()  WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def get_all_by_student(cls):
        query = "SELECT * FROM submissions WHERE student_id = %(student_id)s"
        results = connectToMySQL(DATABASE).query_db(query)
        students = []
        for n in results:
            students.append( cls(n) )
        return students
