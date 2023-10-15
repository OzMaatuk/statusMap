from server import *
import random
import json
import time
from bson import json_util

# Validate address value
def address_validation(address):
    # TODO
    # curl -X POST -d '{
    # "address": {
    #     "regionCode": "US",
    #     "locality": "Mountain View",
    #     "addressLines": ["1600 Amphitheatre Pkwy"]
    # }
    # }' \
    # -H 'Content-Type: application/json' \
    # "https://addressvalidation.googleapis.com/v1:validateAddress?key=YOUR_API_KEY"
    return True

# Get the coordinates for a given address
def get_coordinates(address):
    # TODO: Use a geocoding API to get the coordinates for the address
    # https://maps.googleapis.com/maps/api/geocode/json?address=encoded%20address&key=...
    lat = random.randrange(24, 44)
    lon = random.randrange(0, 60)
    coordinates = (lat, lon)

    # Return the coordinates
    return coordinates

# Update the location-based status for a given address
def update_location_status(address, electricity_availability, water_supply, terrorist_attack, missile_hit):
    coordinates = get_coordinates(address)
    location_status = {
        "address": address,
        "electricity_availability": electricity_availability,
        "water_supply": water_supply,
        "terrorist_attack": terrorist_attack,
        "missile_hit": missile_hit,
        "lat": coordinates[0],
        "lon": coordinates[1],
        "timestamp": time.time()
    }
    db.location_status.insert_one(location_status)
    # TODO: handle already exising addresses
    # Return a success message
    return jsonify({'message': 'Location status updated successfully'})

def get_events():
    # Get all of the location statuses from the database
    location_statuses = db.location_status.find()

    # Create a list of JSON objects for the location statuses
    json_location_statuses = []
    for location_status in location_statuses:
        json_location_statuses.append(location_status)
    
    # return jsonify(json_location_statuses)
    return json.loads(json_util.dumps(json_location_statuses))

# TODO:
# To handle large amount of data, get_events should return only events for last 3000 millisecound.
# https://stackoverflow.com/questions/18233945/query-to-get-last-x-minutes-data-with-mongodb
# And index data by timestamp
# https://www.analyticsvidhya.com/blog/2020/09/mongodb-indexes-pymongo-tutorial/