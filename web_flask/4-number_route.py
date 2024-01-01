#!/usr/bin/python3
"""2-c_route module"""
from flask import Flask, abort


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def root():
    """/: display “Hello HBNB!”"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """/hbnb: display “HBNB”"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """/c/<text>: display C and the text"""
    text_written = "{}".format(text)
    new_text_written = text_written.replace('_', ' ')

    return "C {}".format(new_text_written)


@app.route('/python', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """python_text: display Python and the text"""
    text_written = "{}".format(text)
    new_text_written = text_written.replace('_', ' ')

    return "Python {}".format(new_text_written)


@app.route('/number/<n>', strict_slashes=False)
def number(n):
    """number: display “n is a number” only if n is an integer"""
    try:
        n = int(n)
        return "{} is a number".format(n)
    except ValueError:
        abort(404)


if __name__ == '__main__':
    app.run(debug=True)

