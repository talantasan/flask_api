from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student.db'
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    
    def __repr__(self):
        return f"{self.name}={self.email}"

@app.route('/')
def home():
    std = Student.query.all()
    return render_template('main.html', std=std) 



if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')