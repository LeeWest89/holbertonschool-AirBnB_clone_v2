#!/usr/bin/python3
"""Starts a Flask web app"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states', defaults={'id': None}, strict_slashes=False)
@app.route('/states/<id>')
def states_list(id):
    stored = storage.all("State").values()
    states = sorted(stored, key=lambda state: state.name)
    if id:
        id = "State." + id
    return (render_template('9-states.html', states=states, id=id))


@app.teardown_appcontext
def teardown(exception):
    """Closes storage"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
