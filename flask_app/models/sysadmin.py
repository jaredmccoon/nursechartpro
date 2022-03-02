from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash, session
from flask_app import bcrypt, DATABASE


class Sysadmin:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def save(cls,data):
        query = "INSERT INTO sysadmins (first_name,last_name,email,password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);"
        some_id = connectToMySQL(DATABASE).query_db(query,data)
        return some_id

    @classmethod
    def get_one_by_email(cls, data:dict) -> object:
        query = "SELECT * FROM sysadmins WHERE email = %(email)s"
        result = connectToMySQL(DATABASE).query_db(query,data)
        if result:
            return cls(result[0]) 
        return False

    @staticmethod
    def is_valid(email):
        is_valid = True
        query = "SELECT * FROM emails WHERE email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query,email)
        if len(results) >= 1:
            flash("Email already taken.")
            is_valid=False
        if not EMAIL_REGEX.match(email['email']):
            flash("Email is invalid")
            is_valid=False
        return is_valid

    
    @staticmethod
    def validator(form_data):
        is_valid = True

        if len(form_data['first_name']) < 2:
            is_valid = False
            flash("name is required", "err_first_name")

        if len(form_data['last_name']) < 2:
            is_valid = False
            flash("name is required", "err_last_name")

        if not EMAIL_REGEX.match(form_data['email']):
            is_valid = False
            flash("email not valid", "err_email")

        if len(form_data['password']) < 2:
            is_valid = False
            flash("password not valid", "err_password")

        if form_data['confirm_password'] != form_data['password']:
            is_valid = False
            flash("passwords do not match", "err_confirm_password")

        return is_valid


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
            potential_user = Sysadmin.get_one_by_email({'email': form_data['email']})
            if not potential_user:
                is_valid = False
                flash("not an email", "err_login_email")

            elif not bcrypt.check_password_hash(potential_user.password, form_data['password']):
                is_valid = False
                flash("incorrect password", "err_login_pw")

            else:
                session['userid'] = potential_user.id

        return is_valid