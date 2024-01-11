from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
app.json.sort_keys = False
HOST_IP = os.environ.get('HOST_IP')

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return jsonify(
            {"name": f"{self.name}", 
            "email": f"{self.email}"
            })

class EmployeeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Employee
        include_fk = True

@app.route('/', methods=['GET'])
def home():
    data = [{"name": "talant-api4", "version": "V1",
             "hostname": f"{HOST_IP}"}]
    return jsonify(data)

@app.route('/employee', methods=['GET'])
def get_all():
    emp = Employee.query.all()
    serializer = EmployeeSchema()
    data = serializer.dump(emp, many=True)
    
    return jsonify(data)

@app.route('/employee', methods=['POST'])
def add_employee():
    data = request.get_json()
    emp = Employee(
        name = data.get("name"),
        email = data.get("email")
    )
    db.session.add(emp)
    db.session.commit()
    
    serializer = EmployeeSchema()
    data = serializer.dump(emp)
    
    return jsonify(data)

@app.route('/employee/<int:id>')
def get_employee(id):
    emp = Employee.query.get_or_404(id)
    serializer = EmployeeSchema()
    data = serializer.dump(emp)
    
    return jsonify(data)

@app.route('/employee/<int:id>', methods=['DELETE'])
def del_empoyee(id):
    emp = Employee.query.get_or_404(id)
    db.session.delete(emp)
    db.session.commit()
    
    return jsonify({"message": "deleted"}, 201)

@app.route('/employee/<int:id>', methods=['PUT'])
def update_employee(id):
    emp = Employee.query.get_or_404(id)
    data = request.get_json()
    
    emp.name = data.get("name")
    emp.email = data.get("email")
    
    db.session.add(emp)
    db.session.commit()
    
    serializer = EmployeeSchema()
    data = serializer.dump(emp)
    
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)