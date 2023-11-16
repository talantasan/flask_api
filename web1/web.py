from flask import Flask, render_template
from datetime import datetime
import requests

app = Flask(__name__)

employee_all = requests.get("http://20.55.62.182:8080/employee")

@app.route('/')
def home():
    return render_template('home.html', utc_dt=datetime.utcnow())

@app.route('/employee')
def employee():
    return render_template('employee.html')
            
if __name__ == '__main__':
    app.run(port=5001, host='0.0.0.0', debug=True, threaded=True)