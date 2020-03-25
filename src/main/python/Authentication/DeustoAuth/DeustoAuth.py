#!/usr/bin/python3                                                                                                                                                                                                                           # -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

from src.main.python.Authentication.Interface_Authentication import Interface_Authentication
from src.main.python.User.User import User
from collections import defaultdict
import random
import sys

class DeustoAuth (Interface_Authentication):
    """"
    Class to handle Authentication using Deusto Auth Service
    """
    def __init__(self):
        """
        Constructor
        """
        self.__users = defaultdict( list )
        # user_email -> [ pass, User_object ]
        pass


    """ Override Interface Authentication"""

    def log_in(self, email: str, password: str) -> bool:
        if self.user_exists(email):
            if self.__users[ email ][0] == password:
                return True
        return False


    def create_user(self, user: User) -> str:
        if not self.user_exists(user.get_email()):
            password = random.randint(0, sys.maxsize)
            self.__users[ user.get_email() ].extend( [ str(password), user ] )
            return str(password)
        else:
            return None


    def change_password(self, email: str, password_old: str, password_new: str) -> bool:
        if self.log_in(email, password_old):
            self.__users[ email ][0] = password_new
            return True
        return False


    def delete_user(self, email: str, password: str) -> bool:
        if self.log_in(email, password):
            del self.__users[email]
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
    u1 = User("Inigo", "Lopez-Gazpio", "inigo.lopezgazpio@deusto.es")
    u2 = User("User2", "User2", "user2@deusto.es")
    u3 = User("User3", "User3", "user3@deusto.es")
    u4 = User("User4", "User4", "user4@deusto.es")

    # Create DeustoAuth system
    deustoAuth = DeustoAuth()

    # Create users in DeustoAuth
    pass1 = deustoAuth.create_user(u1)
    print("Created user {} with password {}".format(u1.get_email(), pass1))

    pass2 = deustoAuth.create_user(u2)
    print("Created user {} with password {}".format(u2.get_email(), pass2))

    pass3 = deustoAuth.create_user(u3)
    print("Created user {} with password {}".format(u3.get_email(), pass3))

    # Create erroneus user - duplicated
    pass5 = deustoAuth.create_user(u1)
    print("Created user {} with password {}".format(u1.get_email(), pass5))
    assert(pass5 == None)

    # Login

    result = deustoAuth.log_in(u1.get_email(), pass1);
    assert (result == True)

    result = deustoAuth.log_in(u2.get_email(), pass2);
    assert (result == True)

    result = deustoAuth.log_in(u3.get_email(), pass3);
    assert (result == True)

    result = deustoAuth.log_in(u1.get_email(), pass1 + "a");
    assert (result == False)


    # Change password

    # Non existing user password change
    result = deustoAuth.change_password(u4.get_email(),"asdfasdfasdf","new password");
    assert (result == False)

    # Password No match
    result = deustoAuth.change_password(u1.get_email(), pass1 + "a", "new password");
    assert (result == False)

    # change OK
    result = deustoAuth.change_password(u1.get_email(), pass1, "new password");
    assert (result == True)

    result = deustoAuth.log_in(u1.get_email(), pass1);
    assert (result == False)

    result = deustoAuth.log_in(u1.get_email(), "new password");
    assert (result == True)

    deustoAuth.debug()