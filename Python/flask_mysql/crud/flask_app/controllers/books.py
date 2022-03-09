from flask_app import app
from flask import redirect, render_template,request
from ..models.author import Author
from ..models.book import Book

#main book page with all
@app.route('/books')
def all_books_page():
    return render_template('all_books.html',all_books=Book.all_books())

#create new book
@app.route('/book/new',methods=['POST'])
def new_book():
    data={
        'title':request.form['title'],
        'num_of_pages':request.form['num_of_pages']
    }
    book_id=Book.add_book(data)
    return redirect('/books')

#add favorite
@app.route('/book/addfav',methods=['POST'])
def add_fav_book():
    data={
        'author_id': request.form['author.id'],
        'book.id':request.form['book.id']
    }
    Author.add_favorite(data)
    return redirect(f"/author/{request.form['book.id']}")

#show which authors favorited this book 
@app.route('/books/<int:id>')
def book_fav_author(id):
    data={
        'id':id
    }
    return render_template('book_favorited_by.html',book=Book.get_by_id(data),unfavorite_authors=Book.book_favorited(data))
    