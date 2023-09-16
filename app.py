import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
        return "Hello World!! This is a simple Flask app!"

@app.route('/wassup')
def hello():
        return "Life is Fantastic. Isn't it?"

if __name__ == "__main__":
        app.run()

