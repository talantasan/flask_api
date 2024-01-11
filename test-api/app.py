from flask import Flask, request
from os import environ

app = Flask(__name__)

@app.route('/')
def home():
    return f"{request.host}"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
