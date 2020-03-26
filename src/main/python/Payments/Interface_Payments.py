#!/usr/bin/python3                                                                                                                                                                                                                           # -*- coding: utf-8 -*-
import abc
from abc import ABC, abstractmethod
from src.main.python.User.UserAccount import UserAccount

class Interface_Payments ( ABC ):

    @abstractmethod
    def make_payment(self, email: str, total_amount : float, concept : str) -> str:
        """
        Method to log in an existing user
        Returns receipt id
        """
        pass

    @abstractmethod
    def create_user(self, user: UserAccount, currency : float) -> bool:
        """
        Method to create a new user with some currency
        Returns boolean, True <=> Correct update
        """
        pass

    @abstractmethod
    def update_currency(self, email: str, currency: float) -> bool:
        """
        Method to update currency of user
        Returns boolean, True <=> Correct update
        """
        pass








    
