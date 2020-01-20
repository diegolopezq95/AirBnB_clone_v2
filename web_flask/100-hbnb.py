#!/usr/bin/python3
""" This module starts a Flask web application
"""


from flask import Flask
from flask import render_template
from models import storage, State


app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def state_amenity_list():
    return render_template("100-hbnb.html",
                           state_dict=storage.all('State'),
                           amenity_dict=storage.all('Amenity'),
                           place_dict=storage.all('Place'),
                           user_dict=storage.all('User'))


@app.teardown_appcontext
def teardown(tmp):
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
