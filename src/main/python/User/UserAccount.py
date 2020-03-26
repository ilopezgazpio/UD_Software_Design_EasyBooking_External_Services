#!/usr/bin/python3                                                                                                                                                                                                                           # -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-


class UserAccount():
    """"
    Class to handle Users Accounts
    """
    def __init__(self, name: str, last_name: str, email: str, currency: float):
        """
        Constructor
        """
        self.__name = name
        self.__last_name = last_name
        self.__email = email
        self.__currency = currency

    def get_name (self) -> str:
        return self.__name


    def get_last_name (self) -> str:
        return self.__last_name


    def get_email (self) -> str:
        return self.__email

    def get_currency (self) -> float:
        return self.__currency

    def print (self) -> None:
        print("Printing user\n"
              "Name: {} \n"
              "Last Name: {}\n"
              "Email: {} \n"
              "Currency: {}".format( self.get_name(), self.get_last_name(), self.get_email(), self.get_currency() )
              )


if __name__ == '__main__':

    # Create some users
    u1 = UserAccount("Inigo", "Lopez-Gazpio", "inigo.lopezgazpio@deusto.es", 100)
    u2 = UserAccount("User2", "User2", "user2@deusto.es", -100)
    u3 = UserAccount("User3", "User3", "user3@deusto.es", 0)
    u4 = UserAccount("User4", "User4", "user4@deusto.es", 0)

    # Test all methods
    u1.print()
    u2.print()
    u3.print()
    u4.print()

