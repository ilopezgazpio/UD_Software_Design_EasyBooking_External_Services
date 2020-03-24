#!/usr/bin/python3                                                                                                                                                                                                                           # -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

from src.main.python.Payments import Interface_Payments

class DeustoPay (Interface_Payments):

    """"
    Class to handle Payments using Deusto Pay Service
    """

    def __init__(self):
        """
        Constructor
        """
        super.__init__()
        pass


    """ Override Interface Payments"""
    def make_payment( self,  account : int, total_ammount : float, concept : str) -> str:
        pass


