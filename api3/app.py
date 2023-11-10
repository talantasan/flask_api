from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from marshmallow import Schema, fields


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
app.json.sort_keys = False


db = SQLAlchemy(app)

class Books(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    author = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) :
        return f"{self.name}-{self.author}" 
    
    @classmethod
    def get_all(cls):
        return cls.query.all()
    
    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.ession.commit()

class BooksSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    author = fields.String()
    description = fields.String()
    date_created = fields.DateTime()
    
    
@app.route('/books', methods=['GET'])
def get_books():
    books = Books.get_all()
    serializer = BooksSchema()
    
    data = serializer.dump(books, many=True)
    
    return jsonify(data)
    

@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    
    book = Books(
        name = data.get("name"),
        author = data.get("author"),
        description = data.get("description")
    )
    book.save()
    
    serializer = BooksSchema()
    
    data = serializer.dump(book)
    
    return jsonify(data, 201)
    

@app.route('/books/<int:id>', methods=['GET'])
def get_book_by_id(id):
    pass


@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    pass


@app.route('/books/<int:id>', methods=['DELETE'])
def del_book(id):
    pass

if __name__ == '__main__':
    app.run(debug=True, port=5000)