from flask import Flask, render_template, jsonify, request
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
    if std == []:
        return "<center><h2>No users were found</h2></center>", 204
    else:
        return render_template('main.html', std=std) 

@app.route('/students', methods=['POST'])
def add_user():
    std = Student(name=request.json['name'], email=request.json['email'])
    db.session.add(std)
    db.session.commit()
    return f"new user: {std.id}.{std.name} - {std.email}", 200

@app.route('/students/<int:id>', methods=['GET'])
def get_user(id):
    std = Student.query.get_or_404(id)
    
    return render_template('students.html', std=std)


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')