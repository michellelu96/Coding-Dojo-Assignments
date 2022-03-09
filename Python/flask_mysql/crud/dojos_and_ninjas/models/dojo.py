from dojos_and_ninjas.config.mysqlconnection import connectToMySQL
from .ninja import Ninja


class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.ninjas = []

    # get all dojos
    @classmethod
    def all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL("dojos_and_ninjas").query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    # add a dojo
    @classmethod
    def add_dojo(cls, data):
        query = (
            "INSERT INTO dojos(name,created_at,updated_at)"
            "VALUES(%(name)s,NOW(),NOW());"
        )
        return connectToMySQL("dojos_and_ninjas").query_db(query, data)

    # get all ninjas in one dojo
    @classmethod
    def get_dojo_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL("dojos_and_ninjas").query_db(query, data)
        if results:
            dojo = cls(results[0])
            for row in results:
                n = {
                    "id": row["ninjas.id"],
                    "first_name": row["first_name"],
                    "last_name": row["last_name"],
                    "age": row["age"],
                    "created_at": row["ninjas.created_at"],
                    "updated_at": row["ninjas.updated_at"]
            }
                dojo.ninjas.append(Ninja(n))
                return dojo