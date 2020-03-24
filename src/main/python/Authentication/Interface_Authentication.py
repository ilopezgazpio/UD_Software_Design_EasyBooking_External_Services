#!/usr/bin/python3                                                                                                                                                                                                                           # -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from src.main.python.User import User

class Interface_Authentication ( ABC ):

    @abstractmethod
    def log_in( self, user: User, password: str) -> bool:
        """
        Method to log in an existing user
        Returns boolean, True <=> Correct login
        """
        pass


    @abstractmethod
    def create_user( self, user: User) -> str:
        """
        Method to create a new user with password
        Returns string with password for created user or None if user is not created
        """
        pass


    @abstractmethod
    def change_password(self, user: User, password_old: str, password_new: str) -> bool:
        """
        Method to update password
        Returns boolean, True <=> Correct update
        """
        pass


    @abstractmethod
    def delete_user( self, user: User, password: str) -> bool:
        """
        Method to delete an existing user
        Returns boolean, True <=> Correct deletion
        """
        pass






    
