from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book

class Author:
    def __init__(self,data):
        self.id = data['id']
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.favorite_book=[]
        
    #get all authors
    @classmethod
    def all_authors(cls):
        query="SELECT * FROM authors;"
        results= connectToMySQL("books").query_db(query)
        authors=[]
        for author in results:
            authors.append(cls(author))
        return authors
    
    #add an author
    @classmethod
    def add_author(cls,data):
        query =("INSERT INTO authors(name,created_at,updated_at)"
                "VALUES(%(name)s, NOW(),NOW());"
                )
        return connectToMySQL("books").query_db(query,data)
    
    #add favorite
    @classmethod
    def add_favorite(cls,data):
        query=(
            "INSERT INTO favorites(author_id,book_id)"
            "VALUES(%(author_id)s,%(book_id)s);"
        )
        return connectToMySQL("books").query_db(query,data)

    #show books that have favorite authors
    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM authors "\
            "LEFT JOIN favorites ON authors.id=favorites.author_id "\
            "LEFT JOIN books ON favorites.book_id=books.id "\
            "WHERE authors.id=%(id)s;"
        results= connectToMySQL("books").query_db(query,data)
        for row in results:
            author= cls(results[0])
            if row['books.id'] == None:
                break
            data = {
                'id':row['books.id'],
                'title':row['title'],
                'num_of_pages':row['num_of_pages'],
                'created_at':row['books.created_at'],
                'updated_at':row['books.updated_at']
                }
            author.favorite_book.append(book.Book(data))
        return author
    
    #show books that haven't been favorited
    @classmethod
    def author_favorited(cls,data):
        query = ("SELECT * FROM authors" 
                 "WHERE authors.id"
                "NOT IN ( SELECT author_id FROM favorites WHERE book_id = %(id)s );")
        results = connectToMySQL("books").query_db(query,data)
        authors = []
        if results:
            for row in results:
                authors.append(cls(row))
            return authors