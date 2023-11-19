## Location Status Update

### Overview
This project is a simple web application that allows users to update the status of locations, such as whether they have electricity, water, or have been hit by a missile. The application uses a MongoDB database to store the location status data.

### Dependencies
* Python 3.6 or higher
* Flask
* MongoDB (bson included)
* Maplibre GL

### Usage
1. Install the dependencies:

    pip install flask pymongo python-dotenv

2. Place you maptiler key in the .env file.

3. Start the MongoDB database:

    mongod

4. Run the Flask application:

    python server.py

5. Open a web browser and navigate to http://localhost:5000/map to view the map.

6. To update the status of a location, navigate to http://localhost:5000/form, fill details, and click the "Update" button.

### Containers
1. In the .env file, set the 'MONGODB_CONTAINER_NAME' variable with the MongoDB container name ('statusmap-mongodb').

2. Make sure that you have docker installed and execute the following commands:

        docker network create statusmapnet

        docker build -t statusmap-flask .

        docker run -d --network statusmapnet -p 27017:27017 --name statusmap-mongodb mongo

        docker run -d --network statusmapnet -p 5000:5000 --name statusmap statusmap-flask

### Example
To update the status of a location, click the "Update" button and fill out the form. For example, to update the status of the location "123 Main Street", you would enter the following information into the form:

Address: 123 Main Street

Electricity Available: Checked

Water Supply Available: Checked

Terrorist Attack: Unchecked

Missile Hit: Unchecked

Click the "Update" button to submit the form. The application will then update the status of the location in the database.

### TODO
1. Add OTA login screen
2. Add authentication required for all paths below
3. Add validation for the address field in the form
4. Use a geocoding API to get the coordinates for the address
5. Handle already existing addresses in the database
6. Only return events for the last 3000 milliseconds in the get_events() function
7. Index the location_status collection by timestamp