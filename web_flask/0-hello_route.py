#!/usr/bin/python3
"""start a flask app"""
from flask import Flask

app = Flask(__name__)

#define the route for the root url

app.route('/', strict_slahes=False)
def hello_hbnb():
    """display Hello HBNB! """
    return "Hello HBNB"

if __name__ == "__main>>:
    #start the flask development server
    #listen on all available network interfaces and port 500
    app.run(host='0.0.0.0', port=5000)
