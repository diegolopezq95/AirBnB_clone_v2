#!/usr/bin/python3
""" This module starts a Flask web application
- /: display “Hello HBNB!”
- /hbnb: display “HBNB”
- /c/<text>: display “C ” followed by the value of the
text variable (replace underscore _ symbols with a space )
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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
