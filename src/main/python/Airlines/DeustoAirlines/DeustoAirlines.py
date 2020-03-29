#!/usr/bin/python3                                                                                                                                                                                                                           # -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

from src.main.python.Airlines.Interface_Airlines import Interface_Airlines
from src.main.python.Flight.Flight import Flight
from src.main.python.Flight.Airport import Airport
from collections import defaultdict
import random
import sys
import json
import jsonpickle
from json import JSONEncoder
from datetime import *

class DeustoAirlines (Interface_Airlines):
    """"
    Class to handle Airlines queries using Deusto Airlines Service
    """
    def __init__(self):
        """
        Constructor
        """
        self.__airports = dict( )
        # airport_name -> [ Airport_object ]

        # todo move ???
        self.generate_sample_airports()

        self.__flights = dict( )
        # flight_code -> [ Flight_object ]

        # Create some data
        # todo: improve



    """ Override Interface Authentication"""

    def search_flights(self, **kwparams) -> [Flight]:
        """
        Method to query airline for all flights
        Returns a list of flights

        must be called with these optional parameters
        [
            airport_departure_name: str,

            airport_arrival_name: str,

            free_seats: int,

            price: float,

            departure_date : datetime

        ]

        """
    
        if kwparams:
            airport_departure_name = kwparams.get('airport_departure_name')
            airport_arrival_name = kwparams.get('airport_arrival_name')
            free_seats = kwparams.get('free_seats')
            price = kwparams.get('price')
            departure_date = kwparams.get('departure_date')

            if ( airport_departure_name is None and
                    airport_arrival_name is None and
                    free_seats is None and
                    price is None and
                    departure_date is None):
                return list(self.__flights.values())

            elif ( airport_departure_name is not None and
                    airport_arrival_name is not None and
                    free_seats is not None and
                    price is not None and
                    departure_date is not None):
                return self.search_flights_by_5(kwparams)

            elif ( airport_departure_name is not None and
                   airport_arrival_name is not None and
                   free_seats is not None and
                   price is not None):
                return self.search_flights_by_4(kwparams)

            elif ( airport_departure_name is not None and
                   airport_arrival_name is not None and
                   free_seats is not None ):
                return self.search_flights_by_3(kwparams)

            elif ( airport_departure_name is not None and
                   airport_arrival_name is not None ):
                return self.search_flights_by_2(kwparams)
        else:
            return list(self.__flights.values())


    def search_flights_by_5(self, kwparams):
        return [flight for flight in self.__flights.values() if self.with_same_airports(flight, kwparams) and self.with_free_seats(flight, kwparams) and self.with_price(flight, kwparams) and self.with_time(flight, kwparams)]


    def search_flights_by_4(self, kwparams):
        return [flight for flight in self.__flights.values() if self.with_same_airports(flight, kwparams) and self.with_free_seats(flight, kwparams) and self.with_price(flight, kwparams)]


    def search_flights_by_3(self, kwparams):
        return [ flight for flight in self.__flights.values() if self.with_same_airports(flight, kwparams) and self.with_free_seats(flight, kwparams)]


    def search_flights_by_2(self, kwparams):
        return [ flight for flight in self.__flights.values() if self.with_same_airports(flight, kwparams)]


    def with_time(self, flight, kwparams):
        try:
            parsed_time = datetime.strptime(kwparams['departure_date'], '%Y/%m/%d %H:%M:%S')
        except:
            print("Raised exception - invalid date string")
            return False

        return parsed_time <= flight.get_departure_date() <= parsed_time + timedelta(days=10)


    def with_price(self, flight, kwparams):
        return flight.get_price() <= kwparams['price']


    def with_same_airports(self, flight, kwparams):
        return (flight.get_departure_airport().get_city() == kwparams['airport_departure_name']) and (flight.get_arrival_airport().get_city() == kwparams['airport_arrival_name'])


    def with_free_seats(self, flight, kwparams):
        return flight.get_free_seats() >= kwparams['free_seats']





    """JSON related """
    """def toJSON(self, flight_array):
        json_string = ""

        it = 0
        json_string += "{"
        for flight in flight_array:
            json_string += jsonpickle.encode(flight, unpicklable=False)
            if it < len(flight_array) - 1:
                json_string += ","
            it += 1
        json_string += "}"

        return json_string
    """
    def toJSON(self, flight_array):

        result = jsonpickle.encode(flight_array, unpicklable=False)
        return result


    """Flight related private methods"""
    def flight_exists(self, code):
        if code != None and code.strip() != "" and code in self.__flights.keys():
            return True
        else:
            return False


    """Airport related private methods"""
    def airport_exists(self, code):
        if code != None and code.strip() != "" and code in self.__flights.keys():
            return True
        else:
            return False


    """Sample code generation related"""
    def generate_sample_airports(self):
        a1 = Airport("1111", "Hondarribia")
        a2 = Airport("2222", "Irun")
        a3 = Airport("11AB", "Donostia")
        a4 = Airport("DIY10", "Bilbao")
        a5 = Airport("DA676", "Tabarnia")

        self.__airports[a1.get_city] = a1
        self.__airports[a2.get_city] = a2
        self.__airports[a3.get_city] = a3
        self.__airports[a4.get_city] = a4
        self.__airports[a5.get_city] = a5


    def generate_random_flight(self):
        a1 , a2 = random.sample( list (self.__airports.values() ), k = 2)
        flight = Flight("DA" + str(random.randint(1, 9999)), a1, a2,
                        random.randint(50,150),
                        random.randint(100, 800),
                        datetime.now() + timedelta(days=random.randint(0, 40) , hours = random.randint(0, 23), minutes = random.randint(0, 59)))
        self.__flights[flight.get_code()] = flight


    """Generic private methods"""
    def debug(self):
        print("Printing content...")

        for entry in self.__flights.keys():

            print("Entry Key: {}\n"
                  "Entry values: {}".format(entry, self.__flights[entry]))

            self.__flights[entry].print()



if __name__ == '__main__':


    # Create DeustoAirlines system
    deustoAirlines = DeustoAirlines()

    # Create sample data
    deustoAirlines.generate_random_flight()
    deustoAirlines.generate_random_flight()
    deustoAirlines.generate_random_flight()
    deustoAirlines.generate_random_flight()
    deustoAirlines.generate_random_flight()
    deustoAirlines.generate_random_flight()
    deustoAirlines.generate_random_flight()
    deustoAirlines.generate_random_flight()
    deustoAirlines.generate_random_flight()
    deustoAirlines.generate_random_flight()

    deustoAirlines.generate_random_flight()
    deustoAirlines.generate_random_flight()
    deustoAirlines.generate_random_flight()
    deustoAirlines.generate_random_flight()
    deustoAirlines.generate_random_flight()
    deustoAirlines.generate_random_flight()
    deustoAirlines.generate_random_flight()
    deustoAirlines.generate_random_flight()
    deustoAirlines.generate_random_flight()
    deustoAirlines.generate_random_flight()

    deustoAirlines.generate_random_flight()
    deustoAirlines.generate_random_flight()
    deustoAirlines.generate_random_flight()
    deustoAirlines.generate_random_flight()
    deustoAirlines.generate_random_flight()
    deustoAirlines.generate_random_flight()
    deustoAirlines.generate_random_flight()
    deustoAirlines.generate_random_flight()
    deustoAirlines.generate_random_flight()
    deustoAirlines.generate_random_flight()

    deustoAirlines.generate_random_flight()
    deustoAirlines.generate_random_flight()
    deustoAirlines.generate_random_flight()
    deustoAirlines.generate_random_flight()
    deustoAirlines.generate_random_flight()
    deustoAirlines.generate_random_flight()
    deustoAirlines.generate_random_flight()
    deustoAirlines.generate_random_flight()
    deustoAirlines.generate_random_flight()
    deustoAirlines.generate_random_flight()

    print("Searching all flights")
    flights = deustoAirlines.search_flights()

    """
    [
        airport_departure_name: str,
        airport_arrival_name: str,
        free_seats: int,
        price: float,
        departure_date: datetime
    ]
    """

    """
    # Try searches with seats
    print("Init Search")
    print("----------------------------------------------------------------------------------")
    flights = deustoAirlines.search_flights( airport_departure_name = 'Hondarribia', airport_arrival_name = 'Tabarnia', free_seats = 90)

    for flight in flights:
        flight.print()
    print("----------------------------------------------------------------------------------")
    """

    """
    # Try searches with seats
    print("Init Search")
    print("----------------------------------------------------------------------------------")
    flights = deustoAirlines.search_flights(airport_departure_name='Hondarribia', airport_arrival_name='Tabarnia', free_seats=90, price = 400)

    for flight in flights:
        flight.print()
    print("----------------------------------------------------------------------------------")
    """

    # Try searches with dates
    print("Init Search")
    print("----------------------------------------------------------------------------------")
    flights = deustoAirlines.search_flights(airport_departure_name='Hondarribia', airport_arrival_name='Tabarnia', free_seats=90, price=400, departure_date="2020/03/30 09:00:00")

    for flight in flights:
        flight.print()
    print("----------------------------------------------------------------------------------")

    #deustoAirlines.debug()

    print("JSON related tests")
    result_array = deustoAirlines.search_flights()
    type(result_array)
    print()
    print(deustoAirlines.toJSON(result_array))

