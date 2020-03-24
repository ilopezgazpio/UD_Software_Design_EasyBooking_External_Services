#!/usr/bin/python3                                                                                                                                                                                                                           # -*- coding: utf-8 -*-

import abc

class Interface_Payments ( metaclass = abc.ABCMeta):

    @abc.abstractmethod
    def make_payment( self,  account : int, total_ammount : float, concept : str) -> str:
        """
        Method to make a payment an update users account accordingly.

        Returns payment identifier
        """
        pass





    
