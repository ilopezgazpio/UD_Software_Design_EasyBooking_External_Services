#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
import sys
sys.path.extend(['./src'])
print("Python system path: {} \n\n".format(sys.path))

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

from src.main.python.Payments.DeustoPay.DeustoPay import DeustoPay
from src.main.python.User.UserAccount import UserAccount

import json

app = Flask(__name__)
api = Api(app)

parser = argparse.ArgumentParser(description='Launcher for DeustoPay Microservice')
parser.add_argument('--host', type=str, default="127.0.0.1", help='Local Address in which Restful service will be listening')
parser.add_argument('--port', type=int, default=5000, help='Local port in which Restful service will be listening')
args = parser.parse_args()

print("Python version: {} \n"
      "Current platform: {} \n".format(sys.version, sys.platform))

print("Setting-up EasyBooking Base Services")
print("...")

print("Settinp-up DeustoPay Microservice")
print("...")
deusto_pay = DeustoPay()
print("Settinp-up DeustoPay Microservice [ OK ] ")



"""
Message formats
"""
user_parser = reqparse.RequestParser()
user_parser.add_argument('name', type=str, help= "User name")
user_parser.add_argument('last_name', type=str, help= "User last name")
user_parser.add_argument('email', type=str, help= "User email")
user_parser.add_argument('total_amount', type=float, help= "Payment amount")
user_parser.add_argument('concept', type=str, help= "Payment concept string")
user_parser.add_argument('currency', type=float, help= "Initial currency")



class MicroServices(Resource):

    # curl http://127.0.0.1:5000/
    def get(self):
        return json.dumps({'Status' : 'Working'}), 201


class Pay_MicroService_Make_Payment (Resource):

    # curl http://127.0.0.1:5000/Payments/Make_payment
    def get(self):
        return json.dumps({'Status' : 'Working'}), 201

    # curl http://127.0.0.1:5000/Payments/Make_payment -d '{"email":"inigo.lopezgazpio@deusto.es", "total_amount":"20.5", "concept":"Hello World Payment" }' -X POST -H "Content-Type: application/json" -v
    def post(self):
        user_args = user_parser.parse_args()
        result = deusto_pay.make_payment(user_args.email, user_args.total_amount, user_args.concept)
        return json.dumps({'Result' : result}), 201


class Pay_MicroService_Create_User (Resource):

    # curl http://127.0.0.1:5000/Payments/Create_user
    def get(self):
        return json.dumps({'Status': 'Working'}), 201

    # curl http://127.0.0.1:5000/Payments/Create_user -d '{"name":"Inigo", "last_name":"Lopez-Gazpio", "email":"inigo.lopezgazpio@deusto.es", "currency":"20.5"}' -X POST -H "Content-Type: application/json" -v
    def post(self):
        user_args = user_parser.parse_args()
        user = UserAccount(user_args.name, user_args.last_name, user_args.email, user_args.currency)
        result = deusto_pay.create_user( user )
        return json.dumps({'Result' : result }), 201


class Pay_MicroService_Update_Currency (Resource):

    # curl http://127.0.0.1:5000/Payments/Update_currency
    def get(self):
        return json.dumps({'Status' : 'Working'}), 201

    # curl http://127.0.0.1:5000/Payments/Update_currency -d '{"email":"inigo.lopezgazpio@deusto.es", "currency":"100"}' -X PUT -H "Content-Type: application/json" -v
    def put(self):
        user_args = user_parser.parse_args()
        result = deusto_pay.update_currency( user_args.email, user_args.currency )
        return json.dumps({'Result' : result }), 201


api.add_resource(MicroServices, '/')
api.add_resource(Pay_MicroService_Make_Payment, '/Payments/Make_payment')
api.add_resource(Pay_MicroService_Create_User, '/Payments/Create_user')
api.add_resource(Pay_MicroService_Update_Currency, '/Payments/Update_currency')



if __name__ == '__main__':
    # Debug activates auto-reloading when code changes
    app.run(host=args.host, port=args.port, debug=True)
