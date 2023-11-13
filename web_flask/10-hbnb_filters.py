#!/usr/bin/python3
"""Starts a Flask web app"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    """Creates sorted list of states by name"""
    stored = storage.all("State").values()
    states = sorted(stored, key=lambda state: state.name)
    stored_amenities = storage.all("Amenity").values()
    amenities = sorted(stored_amenities, key=lambda amenity: amenity.name)
    return (render_template('9-states.html', states=states,
                            amenities=amenities))


@app.teardown_appcontext
def teardown(exception):
    """Closes storage"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
