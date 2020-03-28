#!/usr/bin/python3                                                                                                                                                                                                                           # -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from src.main.python.Flight import Flight

class Interface_Airlines ( ABC ):

    @abstractmethod
    def search_flights( self, **kwparams) -> [ Flight ]:
        """
        Method to query airline for all flights
        must be called with these optional parameters
        [
            airport_departure_name: str,

            airport_arrival_name: str,

            free_seats: int,

            price: float,

            departure_date : datetime

        ]
        Returns a list of flights according to the filters passed
        """
        pass






    
