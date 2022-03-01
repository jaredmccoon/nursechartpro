from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash, session
from flask_app import bcrypt, DATABASE




class Student:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.school_id = data['school_id']
    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO students (first_name,last_name,email,password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s,%(school_id)s);"
        some_id = connectToMySQL(DATABASE).query_db(query,data)
        return some_id

    @classmethod
    def get_all_by_school(cls):
        query = "SELECT * FROM students WHERE school_id = %(school_id)s"
        results = connectToMySQL(DATABASE).query_db(query)
        students = []
        for n in results:
            students.append( cls(n) )
        return students

    @classmethod
    def get_one(cls):
        query = "SELECT * FROM students WHERE id = %(id)s"
        result = connectToMySQL(DATABASE).query_db(query)
        return cls(result[0])

    @classmethod
    def get_one_by_email(cls, data:dict) -> object:
        query = "SELECT * FROM students WHERE email = %(email)s"
        result = connectToMySQL(DATABASE).query_db(query,data)
        if result:
            return cls(result[0]) 
        return False


    @staticmethod
    def validator_login(form_data):
        is_valid = True

        if len(form_data['email']) < 2:
            is_valid = False
            
        elif not EMAIL_REGEX.match(form_data['email']):
            is_valid = False

        if len(form_data['password']) < 2:
            is_valid = False

        else:
            potential_user = Student.get_one_by_email({'email': form_data['email']})
            if not potential_user:
                is_valid = False
                flash("not an email", "err_login_email")

            elif not bcrypt.check_password_hash(potential_user.password, form_data['password']):
                is_valid = False
                flash("incorrect password", "err_login_pw")

            else:
                session['userid'] = potential_user.id

        return is_valid
