from flask import Flask, render_template
from datetime import datetime
import requests

app = Flask(__name__)

EMPLOYEE_ENDPOINT = "20.55.62.182"

@app.route('/')
def home():
    return render_template('home.html', utc_dt=datetime.utcnow())

@app.route('/employee')
def employee():
    employee_all = requests.get(f"http://{EMPLOYEE_ENDPOINT}:8080/employee")
    employee_all = employee_all.json()
    return render_template('employee.html', employee=employee_all)

@app.route('/about')
def about():
    return render_template('about.html')
            
if __name__ == '__main__':
    app.run(port=5001, host='0.0.0.0', debug=True, threaded=True)