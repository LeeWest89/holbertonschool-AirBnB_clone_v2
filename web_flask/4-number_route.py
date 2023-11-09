#!/usr/bin/python3
"""starts a Flask web app"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """displays message"""
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """displays message"""
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """displays C and the value of text, underscores are replaced by spaces"""
    return ("C {}".format(text.replace("_", " ")))


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', defaults={"text": "is cool"}, strict_slashes=False)
def python_route(text):
    """displays Python and the value of text"""
    return ("Python {}".format(text.replace("_", " ")))


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """Returns n if n is an int followed by is a number"""
    return ("{} is a number".format(n))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)