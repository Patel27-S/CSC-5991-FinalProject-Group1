from flask import Flask, jsonify
from pymongo import MongoClient
from bson import ObjectId
import json

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client['restaurant']  # Replace 'restaurant' with your database name

# Helper function to convert ObjectId to string
def jsonify_with_objectid(data):
    for document in data:
        document['_id'] = str(document['_id'])
    return jsonify(data)

# API Endpoint to fetch all restaurants
@app.route('/api/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = list(db['restaurants'].find({}))
    return jsonify_with_objectid(restaurants)

# API Endpoint for listing all the restaurants on the basis of 
# Name.
@app.route('/api/restaurants/<Name>', methods=['GET'])
def get_restaurants_seats_available(Name):
    try:
        restaurant = db['restaurants'].find_one({"Name" : Name})
    except:
        print("Please try anothet restaurant")
    return jsonify_with_objectid(restaurant)


# API Endpoint for listing all the restaurants on the basis of 
# number of seats required and available.
# @app.route('/api/restaurants/<Seats_Required>', methods=['GET'])
# def get_restaurants_seats_available(Seats_Required):
#     restaurant = db['restaurants'].find({"Available_Seats" : {"$et": Seats_Required, "$gt": Seats_Required}})
#     return jsonify_with_objectid(restaurant)



if __name__ == '__main__':
    app.run(debug=True)