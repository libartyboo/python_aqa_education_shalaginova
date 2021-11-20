"""Module for exceptions"""


class NotExistCardException(Exception):
    @staticmethod
    def error_message():
        print("Such a card does not exist")


class NotEnoughMoneyException(Exception):
    @staticmethod
    def error_message():
        print("Not enough money!")


class OwnCardException(Exception):
    @staticmethod
    def error_message():
        print("You can't transfer money to the same account!")


class AuthException(Exception):
    ...


class LuhnException(Exception):
    ...
