from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash, session
from flask_app import bcrypt, DATABASE




class School:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.address = data['address']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.adminid = data['admin_id']
    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO schools (name,address,admin_id) VALUES (%(name)s,%(address)s,%(admin_id)s);"
        some_id = connectToMySQL(DATABASE).query_db(query,data)
        return some_id

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM schools WHERE id = %(id)s"
        result = connectToMySQL(DATABASE).query_db(query,data)
        return cls(result[0])
