#!/usr/bin/python3
""" This module starts a Flask web application
"""


from flask import Flask
from flask import render_template
from models import storage, State


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def state_list():
    return render_template("8-cities_by_states.html",
                           my_dict=storage.all('State'))


@app.teardown_appcontext
def teardown(exception):
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
