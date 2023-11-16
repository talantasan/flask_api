from flask import Flask
import requests, threading

app = Flask(__name__)

data = requests.get("http://20.55.62.182:5000/employee")

@app.route('/')
def home():
    return f"""<center> 
            <p><h1>Welcome to home page<h1></p>
            <p>{data.json()}</p>
            </center>"""
            
if __name__ == '__main__':
    app.run(port=5001, host='0.0.0.0', debug=True, threaded=True)