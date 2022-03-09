from recipes import app
from recipes.config.mysqlconnection import connectToMySQL
from flask import flash

class Recipe:
    db="recipes_schema"
    
    def __init__(self,data):
        self.id=data['id']
        self.name=data['name']
        self.description=data['description']
        self.instructions= data['instructions']
        self.under30 = data["under30"]
        self.date_made=data['date_made']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        
    #new recipe
    @classmethod
    def save_recipe(cls,data):
        query ='INSERT INTO recipes (name,description,instructions,under30,date_made,user_id)'\
            "VALUES (%(name)s,%(description)s,%(instructions)s,%(under30)s,%(date_made)s,%(user_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)
      
      #get_all recipes
    @classmethod
    def all_recipes(cls):
        query = "SELECT * FROM recipes;"
        results= connectToMySQL(cls.db).query_db(query)
        all_recipes =[]
        for row in results:
            print(row['date_made'])
            all_recipes.append(cls(row))
        return all_recipes
    
    #get one recipe
    @classmethod
    def get_one(cls,data):
        query="SELECT * FROM recipes WHERE id =%(id)s;"
        results= connectToMySQL(cls.db).query_db(query,data)
        return cls(results[0])
    
    #update recipes
    @classmethod
    def update(cls,data):
        query = "UPDATE recipes SET name=%(name)s, description=%(description)s, instructions=%(instructions)s, under30=%(under30)s, date_made=%(date_made)s,updated_at=NOW()"\
        "WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    #destroy recipes
    @classmethod
    def destroy(cls,data):
        query ="DELETE FROM recipes WHERE id =%(id)s"
        return connectToMySQL(cls.db).query_db(query, data)
    
    #validate recipe!
    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        if len(recipe['name']) < 3:
            is_valid = False
            flash("Name must be at least 3 letters","recipe")
        if len(recipe['instructions']) < 3:
            is_valid = False
            flash("Instructions must be at least 3 letters","recipe")
        if len(recipe['description']) < 3:
            is_valid = False
            flash("Description must be at least 3 letters","recipe")
        if recipe['date_made'] == "":
            is_valid = False
            flash("Please enter a date","recipe")
        return is_valid