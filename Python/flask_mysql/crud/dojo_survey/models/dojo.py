from flask import flash
from dojo_survey.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self,data):
        self.id=data['id']
        self.name=data['name']
        self.location=data['location']
        self.language=data['language']
        self.comment = data['comment']
        self.created_at=data['created_at']
        self.updated_at = data['updated_at']
        
    #get all dojos and languages
    @classmethod
    def get_info(cls):
        query = "SELECT * FROM dojos ORDER BY id DESC LIMIT 1;"
        results = connectToMySQL('dojo_survey').query_db(query)
        return Dojo(results[0])
    
    #save user info
    @classmethod
    def add_info(cls,data):
        query = "INSERT INTO dojos(name,location,language,comment)"\
            "VALUES (%(name)s,%(location)s,%(language)s,%(comment)s);"
        return connectToMySQL('dojo_survey').query_db(query,data)
    
    #validation
    @staticmethod
    def validate_user(survey):
        is_valid = True
        if len(survey['name']) < 3:
            is_valid = False
            flash("Name must be at least 3 characters.")
        if len(survey['location']) < 1:
            is_valid = False
            flash("Must choose a dojo location.")
        if len(survey['language']) < 1:
            is_valid = False
            flash("Must choose a favorite language.")
        if len(survey['comments']) < 3:
            is_valid = False
            flash("Comments must be at least 3 characters.")
        return is_valid