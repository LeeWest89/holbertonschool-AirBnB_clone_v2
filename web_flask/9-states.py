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
    return (render_template('9-states.html', states=states))


@app.route('/states/<id>')
def state_cities(id):
    """Creates sorted list of cities by name for state"""
    state = storage.get("State", id)
    if state:
        cities = sorted(state.cities, key=lambda city: city.name)
        return (render_template('9-states.html', state=state, cities=cities))
    else:
        return render_template('9-states.html', nf=True)


@app.teardown_appcontext
def teardown(exception):
    """Closes storage"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
