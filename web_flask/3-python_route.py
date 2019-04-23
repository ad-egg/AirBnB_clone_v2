#!/usr/bin/python3
"""starts Flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """displays a message"""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """displays a message"""
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_text(ctext):
    """displays "C" followed value of text variable"""
    return "C %s" % ctext.replace("_", " ")

@app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def py_text(ptext="is_cool"):
    """displays "Python" followed by value of text variable"""
    return "Python %s" % ptext.replace("_", " ")

if __name__ == '__main__':
    app.run(host='0.0.0.0')
