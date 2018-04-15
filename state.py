from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest
import sys

from constants import state_boundaries
from point import Point
from raycast import point_inside_shape

app = Flask(__name__)

@app.route("/", methods=['POST'])
def state():
    lat, lon = validate_args(request.form)
    states = []
    for state in state_boundaries:
        state_points = [
            Point(point[0], point[1]) for point in state['border']
        ]
        # Determine if the point lies inside or on the state
        if point_inside_shape(Point(lon, lat), state_points):
            states.append(state['state'])


    return jsonify(states)

def validate_args(args):
    '''
    Confirm that latitude and longitude were passed in
    and that they can both be parsed to float
    '''
    lat = args.get('latitude')
    lon = args.get('longitude')
    if not lat or not lon:
        raise BadRequest('Both latitude and longitude are required in the POST body')
    try:
        lat = float(lat)
        lon = float(lon)
    except ValueError as e:
        raise BadRequest('Both latitude and longitude must be numbers')
    return lat, lon

