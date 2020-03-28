#!/usr/bin/python3                                                                                                                                                                                                                           # -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

from src.main.python.Flight.Airport import Airport
import json
import jsonpickle
from json import JSONEncoder
from time import *
from datetime import *

class Flight():
    """"
    Class to handle Flights
    """

    def __init__(self, code: str, airport_departure: Airport, airport_arrival: Airport, total_seats: int, price: float, departure_date : datetime):
        """
        Constructor
        """
        self.__code = code
        self.__airport_departure = airport_departure
        self.__airport_arrival = airport_arrival
        self.__total_seats = total_seats
        self.__free_seats = total_seats
        self.__price = price
        self.__departure_date = departure_date

        # Todo arrival and departure date


    def get_code(self) -> str:
        return self.__code


    def get_departure_airport(self) -> Airport:
        return self.__airport_departure


    def get_arrival_airport(self) -> Airport:
        return self.__airport_arrival


    def get_total_seats(self) -> int:
        return self.__total_seats


    def get_free_seats(self) -> int:
        return self.__total_seats


    def reserve_seats(self, number: int) -> int:
        if (self.__free_seats < number):
            return 0
        else:
            self.__free_seats -= number
            return self.__free_seats


    def get_price(self) -> float:
        return self.__price


    def get_departure_date(self) -> datetime:
        return self.__departure_date

    def print (self) -> None:
        print("Printing Flight\n"
              "code: {} \n"
              "departure airport: {}\n"
              "arrival airport: {} \n"
              "total seats: {} \n"
              "free seats: {} \n"
              "price: {} \n"
              "departure date: {}".format( self.get_code(), self.get_departure_airport().get_city(), self.get_arrival_airport().get_city(), self.get_total_seats(), self.get_free_seats(), self.get_price(), self.get_departure_date() )
              )


if __name__ == '__main__':

    # Create some Airport
    a1 = Airport("1111", "Hondarribia")
    a2 = Airport("2222", "Castellon")
    a3 = Airport("11AB", "Tabarnia")
    a4 = Airport("DIY10", "Bilbao")


    # Create some Flights
    # datetime(year = 2020, month = 6, day = 10, hour = 5, minute = 55, second = 13)
    f1 = Flight("DA1001", a1, a2, 100, 100, datetime.now())
    f2 = Flight("DA1001", a1, a3, 100, 50, datetime.now() + timedelta(days=1))
    f3 = Flight("DA1001", a1, a4, 100, 300, datetime.now() + timedelta(days=2))
    f4 = Flight("DA1001", a2, a1, 100, 45, datetime.now() + timedelta(days=3))
    f5 = Flight("DA1001", a2, a3, 100, 20, datetime.now() + timedelta(days=4))
    f6 = Flight("DA1001", a3, a4, 100, 600, datetime.now() + timedelta(days=5))
    f7 = Flight("DA1001", a4, a1, 100, 200, datetime.now() + timedelta(days=6))


    # Test all methods
    f1.print()
    f2.print()
    f3.print()
    f4.print()
    f5.print()
    f6.print()
    f7.print()

    # Test Marshalling / Unmarshalling
    json_encoded_1 = jsonpickle.encode(f1, unpicklable=False)
    json_encoded_2 = jsonpickle.encode(f2, unpicklable=False)
    json_encoded_3 = jsonpickle.encode(f3, unpicklable=False)
    json_encoded_4 = jsonpickle.encode(f4, unpicklable=False)

    print(json_encoded_1)
    print(json_encoded_2)
    print(json_encoded_3)
    print(json_encoded_4)

    #print(json.dumps(json_encoded_1, indent=4))
    #json_encoded1 = json.loads(json.dumps(json_encoded_1, indent=4))

    #f5 = jsonpickle.decode(json_encoded_1)
    #f5.print()