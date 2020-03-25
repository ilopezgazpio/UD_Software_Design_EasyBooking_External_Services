#!/usr/bin/python3                                                                                                                                                                                                                           # -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-


class User():

    """"
    Class to handle Users
    """

    def __init__(self, name: str, last_name: str, email: str):
        """
        Constructor
        """
        self.__name = name
        self.__last_name = last_name
        self.__email = email

    def get_name (self) -> str:
        return self.__name


    def get_last_name (self) -> str:
        return self.__last_name


    def get_email (self) -> str:
        return self.__email


    def print (self) -> None:
        print("Printing user\n"
              "Name: {} \n"
              "Last Name: {}\n"
              "Email: {} \n".format( self.get_name(), self.get_last_name(), self.get_email() )
              )


if __name__ == '__main__':

    # Create some users
    u1 = User("Inigo", "Lopez-Gazpio", "inigo.lopezgazpio@deusto.es")
    u2 = User("User2", "User2", "user2@deusto.es")
    u3 = User("User3", "User3", "user3@deusto.es")
    u4 = User("User4", "User4", "user4@deusto.es")

    # Test all methods
    u1.print()
    u2.print()
    u3.print()
    u4.print()

