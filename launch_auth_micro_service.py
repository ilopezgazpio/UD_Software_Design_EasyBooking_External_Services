#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
import sys
sys.path.extend(['./src'])
print("Python system path: {} \n\n".format(sys.path))

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

from src.main.python.Authentication.DeustoAuth.DeustoAuth import DeustoAuth
from src.main.python.User.User import User


app = Flask(__name__)
api = Api(app)

parser = argparse.ArgumentParser(description='Rest microservice tutorial 1')
parser.add_argument('--host', type=str, default="127.0.0.1", help='Local Address in which Restful service will be listening')
parser.add_argument('--port', type=int, default=5000, help='Local port in which Restful service will be listening')
args = parser.parse_args()

print("Python version: {} \n"
      "Current platform: {} \n".format(sys.version, sys.platform))

print("Setting-up EasyBooking Base Services")
print("...")

print("Settinp-up DeustoAuth Microservice")
print("...")
deusto_auth = DeustoAuth()
print("Settinp-up DeustoAuth Microservice [ OK ] ")



"""
Message formats
"""
user_parser = reqparse.RequestParser()
user_parser.add_argument('name', type=str, help= "User name")
user_parser.add_argument('last_name', type=str, help= "User last name")
user_parser.add_argument('email', type=str, help= "User email")
user_parser.add_argument('id_number', type=str, help= "User id number")

user_parser_passwd = reqparse.RequestParser()
user_parser_passwd.add_argument('name', type=str, help= "User name")
user_parser_passwd.add_argument('last_name', type=str, help= "User last name")
user_parser_passwd.add_argument('email', type=str, help= "User email")
user_parser_passwd.add_argument('id_number', type=str, help= "User id number")
user_parser_passwd.add_argument('password', type=str, help= "Current password")

user_parser_passwd2 = reqparse.RequestParser()
user_parser_passwd2.add_argument('name', type=str, help= "User name")
user_parser_passwd2.add_argument('last_name', type=str, help= "User last name")
user_parser_passwd2.add_argument('email', type=str, help= "User email")
user_parser_passwd2.add_argument('id_number', type=str, help= "User id number")
user_parser_passwd2.add_argument('password_old', type=str, help= "Old password")
user_parser_passwd2.add_argument('password_new', type=str, help= "New password")


class MicroServices(Resource):

    # curl http://127.0.0.1:5000/
    def get(self):
        return {'Status': 'Working'}, 201


class Auth_MicroService_Log_in (Resource):

    # curl http://127.0.0.1:5000/Authentication/Log_in
    def get(self):
        return {'Status': 'Working'}, 201

    # curl http://127.0.0.1:5000/Authentication/Log_in -d '{"name":"Inigo", "last_name":"Lopez-Gazpio", "email":"inigo.lopezgazpio@deusto.es", "id_number":"123456789Z", "password":"XXX" }' -X POST -H "Content-Type: application/json" -v
    def post(self):
        user_args = user_parser_passwd.parse_args()
        user = User(user_args.name, user_args.last_name, user_args.email, user_args.id_number)
        result = deusto_auth.log_in(user, user_args.password)
        return {'Result': result}, 201


class Auth_MicroService_Create_User (Resource):

    # curl http://127.0.0.1:5000/Authentication/Create_user
    def get(self):
        return {'Status': 'Working'}, 201

    # curl http://127.0.0.1:5000/Authentication/Create_user -d '{"name":"Inigo", "last_name":"Lopez-Gazpio", "email":"inigo.lopezgazpio@deusto.es", "id_number":"123456789Z"}' -X POST -H "Content-Type: application/json" -v
    def post(self):
        user_args = user_parser.parse_args()
        user = User(user_args.name, user_args.last_name, user_args.email, user_args.id_number)
        user.print()
        result = deusto_auth.create_user( user )
        return { 'Result' : result }, 201


class Auth_MicroService_Change_Password (Resource):

    # curl http://127.0.0.1:5000/Authentication/Change_password
    def get(self):
        return {'Status': 'Working'}, 201

    # curl http://127.0.0.1:5000/Authentication/Change_password -d '{"name":"Inigo", "last_name":"Lopez-Gazpio", "email":"inigo.lopezgazpio@deusto.es", "id_number":"123456789Z", "password_old":"XXX", "password_new":"XXX"}' -X PUT -H "Content-Type: application/json" -v
    def put(self):
        user_args = user_parser_passwd2.parse_args()
        user = User(user_args.name, user_args.last_name, user_args.email, user_args.id_number)
        user.print()
        result = deusto_auth.change_password( user, user_args.password_old, user_args.password_new )
        return { 'Result' : result }, 201


class Auth_MicroService_Delete_User (Resource):

    # curl http://127.0.0.1:5000/Authentication/Delete_user
    def get(self):
        return {'Status': 'Working'}, 201

    # curl http://127.0.0.1:5000/Authentication/Delete_user -d '{"name":"Inigo", "last_name":"Lopez-Gazpio", "email":"inigo.lopezgazpio@deusto.es", "id_number":"123456789Z", "password":"XXX" }' -X DELETE -H "Content-Type: application/json" -v
    def delete (self):
        user_args = user_parser_passwd.parse_args()
        user = User(user_args.name, user_args.last_name, user_args.email, user_args.id_number)
        result = deusto_auth.delete_user(user, user_args.password)
        return {'Result': result}, 201


api.add_resource(MicroServices, '/')
api.add_resource(Auth_MicroService_Log_in, '/Authentication/Log_in')
api.add_resource(Auth_MicroService_Create_User, '/Authentication/Create_user')
api.add_resource(Auth_MicroService_Change_Password, '/Authentication/Change_password')
api.add_resource(Auth_MicroService_Delete_User, '/Authentication/Delete_user')


if __name__ == '__main__':
    # Debug activates auto-reloading when code changes
    app.run(host=args.host, port=args.port, debug=True)