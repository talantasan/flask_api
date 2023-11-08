from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    author = db.Column(db.String(50))
    
    def __repr__(self):
        return f"{self.name}: {self.author}"

@app.route('/')
def hello():
    return "<h1>Hello</h1>"

@app.route('/books')
def get_books():
    lst_books = []
    books = Books.query.all()
    for book in books:
         data = {
             "name": book.name,
             "author": book.author
         }
         lst_books.append(data)
    return jsonify(lst_books)


@app.route('/books/<int:id>')
def get_book_id(id):
    book = Books.query.get_or_404(id)
    return jsonify({"name": book.name, "author": book.author}) 

@app.route('/books', methods=['POST'])
def add_book():
    book = Books(name=request.json['name'], author=request.json['author'])
    db.session.add(book)
    db.session.commit()
    
    return jsonify({"book added": book.name})

@app.route('/books/<int:id>', methods = ['DELETE'])
def delete_book(id):
    book = Books.query.get(id)
    if book is None:
        return jsonify({"Book not found": 404})
    else:
        db.session.delete(book)
        db.session.commit()
        return jsonify({"deleted book": book.name})
