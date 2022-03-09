from flask_app import app
from flask import redirect, render_template,request
from ..models.author import Author
from ..models.book import Book

#main page to show all the authors
@app.route('/')
@app.route('/authors')
def all_authors_page():
    return render_template('all_authors.html',all_authors=Author.all_authors())

#add the authors
@app.route('/create/author',methods=['POST'])
def create_an_author():
    data={
        'name': request.form['author_name']
    }
    author_id=Author.add_author(data)
    return redirect('/authors')

#show the author favorite books
@app.route('/authors/<int:id>')
def author_favorites(id):
    data={
        'id':id
    }
    return render_template('author_favorites.html',author=Author.get_by_id(data),books=Book.book_favorited(data))


#add the favorites
@app.route('/author/addfav',methods=['POST'])
def add_fav_author():
    data={
        'author_id': request.form['author.id'],
        'book.id':request.form['book.id']
    }
    Author.add_favorite(data)
    return redirect(f"/author/{request.form['author_id']}")