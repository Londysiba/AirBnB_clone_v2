#!/usr/bin/python3
"""A script that starts a Flask web application
"""
from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """return hello hbhb
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """return HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    """return text given"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python/', defaults={'text': 'is_cool'})
@app.route('/python/<text>', strict_slashes=False)
def display(text):
    """display “Python ”, followed by the value of the text"""
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def num_display(n):
    """display “n is a number” only"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_html(n):
    """display HTML is "n" is a number only"""
    return render_template('5-number.html', name=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def num_html_even_odd(n):
    """display HTML is "n" is a number only
    H1 tag: Number: n is even|odd"""
    return render_template('6-number_odd_or_even.html', name=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
