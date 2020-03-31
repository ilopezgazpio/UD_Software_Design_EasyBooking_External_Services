#!/usr/bin/python3
# -*- coding: utf-8 -*-

###########################
# IMPORTANT NOTE
# INSTALL LIBRARIES:
# JSON
# PYMONGO
# JSONPICLE
############################


import argparse
import sys

sys.path.extend(['./src'])
print("Python system path: {} \n\n".format(sys.path))

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

from src.main.python.Airlines.DeustoAirlines.DeustoAirlines import DeustoAirlines
from src.main.python.Flight.Flight import Flight
from src.main.python.Flight.Airport import Airport

import json

app = Flask(__name__)
api = Api(app)

parser = argparse.ArgumentParser(description='Launcher for DeustoAirlines Microservice')
parser.add_argument('--host', type=str, default="127.0.0.1", help='Local Address in which Restful service will be listening')
parser.add_argument('--port', type=int, default=5000, help='Local port in which Restful service will be listening')
args = parser.parse_args()

print("Python version: {} \n"
      "Current platform: {} \n".format(sys.version, sys.platform))

print("Setting-up EasyBooking Base Services")
print("...")

print("Settinp-up DeustoAirlines Microservice")
print("...")
deusto_airlines = DeustoAirlines()
print("Settinp-up DeustoAirlines Microservice [ OK ] ")


"""
Message formats
"""
flight_parser = reqparse.RequestParser()
flight_parser.add_argument('airport_departure_name', type=str, help= "Departure airport name", required=False)
flight_parser.add_argument('airport_arrival_name', type=str, help= "Arrival airport name", required=False)
flight_parser.add_argument('free_seats', type=int, help= "Minimum number of free seats in flight", required=False)
flight_parser.add_argument('price', type=float, help= "Maximum price of flight", required=False)
flight_parser.add_argument('departure_date', type=str, help= "String to be parsed to datetime value following %Y/%m/%d %H:%M:%S format", required=False)

class MicroServices(Resource):

    # curl http://127.0.0.1:5000/
    def get(self):
        return json.dumps({'Status': 'Working'}), 201


class Airlines_MicroService_Search_Flights (Resource):

    # curl http://127.0.0.1:5000/Airlines/Search_Flights
    def get(self):
        return json.dumps({'Status': 'Working'}), 201

    # curl http://127.0.0.1:5000/Airlines/Search_Flights -d '{ }' -X POST -H "Content-Type: application/json" -v
    # curl http://127.0.0.1:5000/Airlines/Search_Flights -d '{"airport_departure_name":"Hondarribia", "airport_arrival_name":"Tabarnia" }' -X POST -H "Content-Type: application/json" -v
    # curl http://127.0.0.1:5000/Airlines/Search_Flights -d '{"airport_departure_name":"Hondarribia", "airport_arrival_name":"Tabarnia", "free_seats":"100" }' -X POST -H "Content-Type: application/json" -v
    # curl http://127.0.0.1:5000/Airlines/Search_Flights -d '{"airport_departure_name":"Hondarribia", "airport_arrival_name":"Tabarnia", "free_seats":"100", "price":"700" }' -X POST -H "Content-Type: application/json" -v
    # curl http://127.0.0.1:5000/Airlines/Search_Flights -d '{"airport_departure_name":"Hondarribia", "airport_arrival_name":"Tabarnia", "free_seats":"100", "price":"700", "departure_date":"2020/04/03 09:00:00" }' -X POST -H "Content-Type: application/json" -v
    def post(self):
        flight_args = flight_parser.parse_args()

        deusto_airlines.generate_random_flight()
        deusto_airlines.generate_random_flight()
        deusto_airlines.generate_random_flight()
        deusto_airlines.generate_random_flight()
        deusto_airlines.generate_random_flight()


        result = deusto_airlines.search_flights(
            airport_departure_name = flight_args.airport_departure_name,
            airport_arrival_name   = flight_args.airport_arrival_name,
            free_seats             = flight_args.free_seats,
            price                  = flight_args.price,
            departure_date         = flight_args.departure_date)

        return deusto_airlines.toJSON(result), 201



api.add_resource(MicroServices, '/')
api.add_resource(Airlines_MicroService_Search_Flights, '/Airlines/Search_Flights')


if __name__ == '__main__':
    # Debug activates auto-reloading when code changes
    app.run(host=args.host, port=args.port, debug=True)
