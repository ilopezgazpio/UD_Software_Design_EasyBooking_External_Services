#!/usr/bin/python3                                                                                                                                                                                                                           # -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

import json
import jsonpickle
from json import JSONEncoder

class Airport():
    """"
    Class to handle Airports
    """

    def __init__(self, code: str, city: str):
        """
        Constructor
        """
        self.__code = code
        self.__city = city


    def get_code(self) -> str:
        return self.__code


    def get_city(self) -> str:
        return self.__city


    def print (self) -> None:
        print("Printing airport\n"
              "Code: {} \n"
              "City: {}\n".format( self.get_code(), self.get_city())
              )


if __name__ == '__main__':

    # Create some airports
    a1 = Airport("1111", "Hondarribia")
    a2 = Airport("2222", "Irun")
    a3 = Airport("11AB", "Donostia")
    a4 = Airport("DIY10", "Bilbao")

    # Test Marshalling / Unmarshalling
    json_encoded_1 = jsonpickle.encode(a1, unpicklable=True)
    json_encoded_2 = jsonpickle.encode(a2, unpicklable=True)
    json_encoded_3 = jsonpickle.encode(a3, unpicklable=True)
    json_encoded_4 = jsonpickle.encode(a4, unpicklable=True)

    print(json_encoded_1)
    print(json_encoded_2)
    print(json_encoded_3)
    print(json_encoded_4)

    print(json.dumps(json_encoded_1, indent=4))
    json_encoded1 = json.loads(json.dumps(json_encoded_1, indent=4))

    a5 = jsonpickle.decode(json_encoded_1)
    a5.print()




