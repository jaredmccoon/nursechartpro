from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash, session
from flask_app import bcrypt, DATABASE


class Medication:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # left join to medications has submissions
    @classmethod
    def save(cls,data):
        query = "INSERT INTO medications (name) VALUES (%(name)s);"
        some_id = connectToMySQL(DATABASE).query_db(query,data)
        return some_id