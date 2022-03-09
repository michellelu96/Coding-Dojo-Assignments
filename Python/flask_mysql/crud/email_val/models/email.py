from email_val.config.mysqlconnection import connectToMySQL
import re
from flask import flash

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class Email:
    db= "email_address_schema"
    def __init__(self,data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    #show all emails
    @classmethod
    def all_emails(cls):
        query = "SELECT * FROM emails;"
        results = connectToMySQL(cls.db).query_db(query)
        emails = []
        for row in results:
            emails.append( cls(row) )
        return emails
    
    #create a new email 
    @classmethod
    def save(cls,data):
        query = "INSERT INTO emails (email,created_at)"\
            "VALUES(%(email)s,NOW());"
        return connectToMySQL(cls.db).query_db(query,data)
    
    #validation
    @staticmethod
    def is_valid(email):
        is_valid = True
        query = "SELECT * FROM emails WHERE email = %(email)s;"
        results = connectToMySQL(Email.db).query_db(query,email)
        if len(results) >= 1:
            flash("Email already taken.")
            is_valid = False
        if not EMAIL_REGEX.match(email['email']):
            flash("Invalid Email!")
            is_valid = False
        return is_valid
    
    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM emails WHERE id=%(id)s;"
        results = connectToMySQL(Email.db).query_db(query, data)
        return results
    