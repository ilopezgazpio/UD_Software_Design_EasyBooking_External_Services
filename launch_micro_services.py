#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
sys.path.extend(['./src'])
print("Python system path: {} \n".format(sys.path))

from src.main.python.Authentication.DeustoAuth.DeustoAuth import DeustoAuth




if __name__ == '__main__':

    print("Python version: {} \n"
          "Current platform: {} \n".format(sys.version, sys.platform))

    print("Setting-up EasyBooking Base Services")
    print("...")

    print("Settinp-up DeustoAuth Microservice")
    print("...")
    deusto_auth = DeustoAuth()
    print("Settinp-up DeustoAuth Microservice [ OK ] ")