from flask import Flask
from os import environ

app = Flask(__name__)
MY_DB_HOST = environ.get('DB_NAME')

@app.route('/')
def home():
    return f"Hello World {MY_DB_HOST}"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
