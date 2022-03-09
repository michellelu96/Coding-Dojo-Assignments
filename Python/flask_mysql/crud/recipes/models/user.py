from recipes.config.mysqlconnection import connectToMySQL
from recipes import app
import re
from flask import flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    db="recipes_schema"
    def __init__(self,data):
        self.id =data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email=data['email']
        self.password = data['password']
        self.created_at=data['created_at']
        self.updated_at = data['updated_at']
        
    #make new people
    @classmethod
    def save(cls,data):
        query ="INSERT INTO users(first_name,last_name,email,password)"\
            "VALUES(%(first_name)s,%(last_name)s,%(email)s,%(password)s);"
        return connectToMySQL(cls.db).query_db(query,data)
    
    #get all users
    @classmethod
    def get_all_users(cls):
        query="SELECT * FROM users"
        results= connectToMySQL(cls.db).query_db(query)
        users =[]
        for row in results:
            users.append(cls(row))
        return users
    
    #get user by email
    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    #get user by id
    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users WHERE id= %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        return cls(results[0])
    
    #get recipes by user
    @classmethod
    def get_all_user(cls,data):
        query="SELECT * FROM users LEFT JOIN recipes ON users.id=recipes.user_id WHERE users.id=%(id)s;"
        results= connectToMySQL(cls.db).query_db(query,data)
        return cls(results[0])
    
    #validate registering
    @staticmethod
    def validate_register(user):
        is_valid = True
        users = User.get_by_email(user)
        if users:
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
            is_valid = False
        return is_valid
    
    #validate login
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