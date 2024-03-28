#!/usr/bin/python3
#start a flask web application
from flask import Flask
app = Flask(__name__)

#Define the route for the url
@app,route('/', strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNH'. """
    return "HelloHBNB!"
#define the route for /hbnb
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB'. """
    return "HBNB"

#Define the route for '/c/<text>'
@app.route('/c/<text>', strict_slashes=False)
def c_with_text(text):
    """Displays 'c' followed by the value of <text>."""
    #Replace underscore with spaces in the text
    formatted_text = text.replace('_', ' ')
    return "c ()".format(formatted_text)

if __name__ == "__main__":
    app.run(host='0.0.0.0, port=5000)
