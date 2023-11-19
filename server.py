# import logging
import pymongo
from flask import Flask, jsonify, request, render_template
from dotenv import load_dotenv
from os import getenv
import utils
load_dotenv()

# Connect to the MongoDB database
host = getenv("MONGODB_CONTAINER_NAME" ,"localhost")
api_key = getenv("MAPTILER_KEY" ,"")
client = pymongo.MongoClient(host, 27017)
db = client['events_database']

app = Flask(__name__)

# TODO: add OTA login screen
# TODO: add authentication required for all paths below

# Get the map screen
@app.route('/map')
def map():
    return render_template('map.html', api_key=api_key)

# Get data from db
@app.route('/get_events', methods=['GET'])
def events():
    return utils.get_events()

@app.route('/form', methods=['GET'])
def form():
    return render_template('form.html')

# Update the status update screen
@app.route('/update', methods=['POST'])
def update():
    # Get the address, electricity_availability, water_supply, terrorist_attack, and missile_hit from the request
    address = request.form['address']
    if (not utils.address_validation(address)): return jsonify({'message': 'Must include valid address'})
    if (request.form.get('electricity')): electricity_availability = True
    else: electricity_availability = False
    if (request.form.get('water')): water_supply = True
    else: water_supply = False
    if (request.form.get('terrorist')): terrorist_attack = True
    else: terrorist_attack = False 
    if (request.form.get('missile')): missile_hit = True
    else: missile_hit = False

    # Update the location-based status for the given address
    return utils.update_location_status(address, electricity_availability, water_supply, terrorist_attack, missile_hit)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
