from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash, session
from flask_app import bcrypt, DATABASE




class Course:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.teacher_id = data['teacher_id']
        self.school_id = data['school_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO courses (name,teacher_id,school_id) VALUES (%(name)s,%(teacher_id)s,%(school_id)s);"
        some_id = connectToMySQL(DATABASE).query_db(query,data)
        return some_id

    @classmethod
    def get_all_by_school(cls):
        query = "SELECT * FROM courses WHERE school_id = %(id)s"
        results = connectToMySQL(DATABASE).query_db(query)
        courses = []
        for n in results:
            courses.append( cls(n) )
        return courses

    @classmethod
    def get_all_by_teacher(cls):
        query = "SELECT * FROM courses WHERE teacher_id = %(teacher_id)s"
        results = connectToMySQL(DATABASE).query_db(query)
        courses = []
        for n in results:
            courses.append( cls(n) )
        return courses

    @classmethod
    def get_one(cls):
        query = "SELECT * FROM courses WHERE id = %(id)s"
        result = connectToMySQL(DATABASE).query_db(query)
        return cls(result[0])
