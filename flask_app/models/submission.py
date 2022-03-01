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

    # @classmethod
    # def save(cls,data):
    #     query = "INSERT INTO submissions (first_name,last_name,email,age,password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(age)s,%(password)s);"
    #     some_id = connectToMySQL(DATABASE).query_db(query,data)
    #     return some_id