#!/usr/bin/python3                                                                                                                                                                                                                           # -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

from src.main.python.Payments.Interface_Payments import Interface_Payments
from src.main.python.User.UserAccount import UserAccount
from collections import defaultdict
import random
import sys

class DeustoPay (Interface_Payments):
    """"
    Class to handle Payments using Deusto Pay Service
    """
    def __init__(self):
        """
        Constructor
        """
        self.__users = defaultdict(list)
        # user_email -> [ currency, User_object ]
        pass


    """ Override Interface Payments"""
    def make_payment(self, email: str, total_amount: float, concept: str) -> str:
        """
        Method to log in an existing user
        Returns receipt id
        """
        if self.user_exists(email):
            if self.__users[email][0] >= total_amount:
                self.__users[email][0] -= total_amount
                return "R" + str(random.randint(0, sys.maxsize)) + "_C:" + concept
        return False


    def create_user(self, user: UserAccount) -> bool:
        """
        Method to create a new user with password and some currency
        Returns boolean, True <=> Correct creation
        """
        if not self.user_exists(user.get_email()):
            self.__users[user.get_email()].extend([user.get_currency(), user])
            return True
        else:
            return False


    def update_currency(self, email: str, currency: float) -> bool:
        """
        Method to update currency of user
        Returns boolean, True <=> Correct update
        """
        if self.user_exists(email):
            self.__users[email][0] += currency
            return True
        return False


    """Private methods"""
    def user_exists(self, email):
        if email != None and email.strip() != "" and email in self.__users.keys():
            return True
        else:
            return False


    def debug(self):
        print("Printing content...")

        for entry in self.__users.keys():

            print("Entry Key: {}\n"
                  "Entry values: {}".format(entry, self.__users[entry]))

            self.__users[entry][1].print()




if __name__ == '__main__':

    # Create some users
    u1 = UserAccount("Inigo", "Lopez-Gazpio", "inigo.lopezgazpio@deusto.es", 100.1)
    u2 = UserAccount("User2", "User2", "user2@deusto.es", 50.0)
    u3 = UserAccount("User3", "User3", "user3@deusto.es", -20.5)
    u4 = UserAccount("User4", "User4", "user4@deusto.es", 0)

    # Create DeustoPay system
    deustoPay = DeustoPay()

    # Create users in DeustoAuth
    result1 = deustoPay.create_user(u1)
    assert (result1 == True)
    print("Created user {} with currency {}".format(u1.get_email(), u1.get_currency()))

    result2 = deustoPay.create_user(u2)
    assert (result2 == True)
    print("Created user {} with currency {}".format(u2.get_email(), u2.get_currency()))

    result3 = deustoPay.create_user(u3)
    assert (result3 == True)
    print("Created user {} with currency {}".format(u3.get_email(), u3.get_currency()))

    # Create erroneus user - duplicated
    result4 = deustoPay.create_user(u1)
    assert (result4 == False)

    # Test make payment
    result = deustoPay.make_payment(u4.get_email(), 100, "Invalid user payment")
    assert (result == False)

    result = deustoPay.make_payment(u3.get_email(), 100, "Invalid payment - No Money")
    assert (result == False)

    result = deustoPay.make_payment(u2.get_email(), 40, "OK payment")
    assert (result != False)

    result = deustoPay.make_payment(u2.get_email(), 40, "Invalid payment - No Money")
    assert (result == False)

    result = deustoPay.make_payment(u1.get_email(), 50.05, "OK payment")
    assert (result != False)

    result = deustoPay.make_payment(u1.get_email(), 50.05, "OK payment")
    assert (result != False)

    result = deustoPay.make_payment(u1.get_email(), 0.0000001, "Invalid payment - No Money")
    assert (result == False)

    #Test Update currency

    result = deustoPay.update_currency(u1.get_email(), 1)
    assert (result == True)
    result = deustoPay.make_payment(u1.get_email(), 1, "OK payment")
    assert (result != False)
    result = deustoPay.make_payment(u1.get_email(), 1, "Invalid payment - No Money")
    assert (result == False)

    result = deustoPay.update_currency(u4.get_email(), 1)
    assert (result == False)

    deustoPay.debug()

    result = deustoPay.update_currency(u3.get_email(), 21)
    assert (result == True)
    result = deustoPay.make_payment(u3.get_email(), 0.5, "OK payment")
    assert (result != False)
    result = deustoPay.make_payment(u3.get_email(), 1, "Invalid payment - No Money")
    assert (result == False)

    deustoPay.debug()






