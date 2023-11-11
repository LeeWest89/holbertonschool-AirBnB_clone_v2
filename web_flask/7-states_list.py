#!/usr/bin/python3
"""Starts a Flask web app"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    stored = storage.all("State")
    states = sorted(stored, key=lambda state: state.name)
    return (render_template('7-states_list.html', states=states))


@app.teardown_appcontext
def teardown(exception):
    """Closes storage"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
