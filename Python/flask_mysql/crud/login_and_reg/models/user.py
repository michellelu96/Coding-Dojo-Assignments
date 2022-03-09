from login_and_reg import app
from login_and_reg.config.mysqlconnection import connectToMySQL
import re
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask import flash
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    db="login"
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email_address = data['email']
        self.password= data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        
    #save new user
    @classmethod
    def save_user(cls,data):
        query = "INSERT INTO users (first_name,last_name,email,password)"\
        "VALUES (%(first_name)s,%(last_name)s,%(email)s, %(password)s);"
        return connectToMySQL(cls.db).query_db(query, data)
    
    #get the email to look in database, see if it's there
    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    #get info by id, don't need check length!, just loading info
    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users WHERE id= %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        if results:
            return cls(results[0])
            
    
    
    #validate stuff for registering
    @staticmethod
    def validate_register(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(User.db).query_db(query,user)
        if len(results) >= 1:
            flash("Email already taken.","register")
            is_valid=False
        if len(user['first_name']) <3:
            is_valid = False
            flash("First Name must be at least 3 letters","register")
        if len(user['last_name']) <3:
            is_valid = False
            flash("Last Name must be at least 3 letters","register")
        if len(user['password']) < 8:
            flash('Password must be at least 8 letters',"register")
            is_valid = False
        if len(user['email']) < 3:
            flash('Email must be at least 3 letters',"register")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash('Invalid email address!',"register")
            is_valid = False
        if user['password'] != user['confirm_password']:
            flash("Passwords don't match","register")
        return is_valid
    
    #validate login, make sure it matches!
    @staticmethod
    def validate_login(data):
        is_valid= True
        user = User.get_by_email(data)
        if not user:
            flash("Invalid Login","login")
            is_valid= False
        elif not bcrypt.check_password_hash(user.password,data['password']):
            flash("Invalid password","login")
            is_valid= False
        return is_valid