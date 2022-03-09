from flask_app.config.sqlconnection import connectToMySQL
    
class User:
    def __init__(self,data):
        self.id =data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email =data['email']
        self.created_at=data['created_at']
        self.updated_at =data['updated_at']
        
# GET all of the users
    @classmethod
    def get_all_users(cls):
        query = 'SELECT* FROM users;'
        results = connectToMySQL('mydb').query_db(query)
        users=[]
        for user in results:
            users.append(cls(user))
        return users
    
#create new user
    @classmethod
    def create_user(cls,data):
        query="INSERT INTO users(first_name,last_name,email,created_at,updated_at)"\
            "VALUES (%(first_name)s,%(last_name)s,%(email)s,NOW(),NOW());"
        results = connectToMySQL('mydb').query_db(query,data)
        return results
        
#update the user
    @classmethod
    def update(cls,data):
        query = "UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('mydb').query_db(query,data)

#delete user
    @classmethod
    def delete_user(cls,data):
        query="DELETE FROM users WHERE id=%(id)s;"
        return  connectToMySQL('mydb').query_db(query,data)

#look at user info
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM users WHERE id=%(id)s;"
        results = connectToMySQL('mydb').query_db(query,data)
        if results== True:
            return  cls(results[0])
        else:
            return None