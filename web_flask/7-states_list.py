#!/usr/bin/python3
"""Starts a Flask web app"""

from flask import Flask, render_template
from models.__init__ import storage

app = Flask(__name__)


@app.route('/state_list', strict_slashes=False)
def states_list():
    states = storage.all("State")
    sort = sorted(states, key=lambda state: state.name)
    return (render_template('7-states_list.html', states=sort))


@app.teardown_appcontext
def teardown(exception):
    """Closes storage"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
