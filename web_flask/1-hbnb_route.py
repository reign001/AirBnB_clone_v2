#!/usr/bin/python3

#a script that starts a Flask web application

from flask import Flask
"""deploying the falsk app"""
app = Flask(__name__)

"""defining the route"""
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """displays "hello HBNB!" ."""
    return "Hello HBNB"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB', """
    return 'HBNB'

if __name__ == "__main__":
    #start the flask development server
    #listen on all available port and port 5000
    app.run(host="0.0.0.0, port=5000)
