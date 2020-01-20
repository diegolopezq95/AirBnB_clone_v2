#!/usr/bin/python3
""" This module starts a Flask web application
- /: display “Hello HBNB!”
- /hbnb: display “HBNB”
- /c/<text>: display “C ” followed by the value of the
text variable (replace underscore _ symbols with a space )
- /python/(<text>): display “Python ”, followed by the value of
the text variable (replace underscore _ symbols with a space )
- /number/<n>: display “n is a number” only if n is an integer
"""


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """
    listen on 0.0.0.0, port 5000 return Hello HBNB!
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """
    return HBNB
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def C_text(text):
    """
    Displays C followed by the value of the text variable
    """
    return "C {}".format(text).replace("_", " ")


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def Python_text(text='is cool'):
    """
    Displays Python followed by the value of the text variable
    """
    return "Python {}".format(text).replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def n_number(n):
    """
    Displays a number n only if it is an integer
    """
    return "{} is a number".format(n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
