from dojos_and_ninjas.config.mysqlconnection import connectToMySQL


class Ninja:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    # add a new ninja to the dojo
    @classmethod
    def add_new_ninja(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name,age,created_at,updated_at,dojo_id)"\
        "VALUES (%(first_name)s, %(last_name)s, %(age)s,NOW(),NOW(), %(dojo_id)s);"
        results = connectToMySQL("dojos_and_ninjas").query_db(query, data)
        return results
