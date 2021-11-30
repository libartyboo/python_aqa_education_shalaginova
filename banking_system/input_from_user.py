"""Module for inputs from players"""
import string
import random


class InputFromUser:
    """Class for inputs from players"""
    menu = '''1. Create an account
2. Log into account
0. Exit\n'''
    login_card_folder = "Enter your card number:\n"
    login_pin_folder = "Enter your PIN:\n"
    user_actions_menu = '''1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit\n'''
    income = "Enter income:\n"
    transfer_card = '''Transfer
Enter card number:\n'''
    transfer_money = "Enter how much money you want to transfer:\n"
    gen_captcha = None
    captcha = "Prove that you are not a robot. Enter CAPTCHA: "

    def get_menu_item(self):
        """Prints Menu options, gets input and validate value, returns input"""
        while True:
            try:
                user_answer = int(input(self.menu))
                return user_answer
            except ValueError:
                print("Invalid input. Insert the number")

    def login_get_card_number(self):
        """Asks user enter card number and returns input"""
        user_answer = input(self.login_card_folder)
        return user_answer

    def login_get_pin(self):
        """Asks user enter pin and returns input"""
        while True:
            try:
                user_answer = int(input(self.login_pin_folder))
                return user_answer
            except ValueError:
                print("Invalid input. Insert the number")

    def get_user_actions(self):
        """Prints Menu options, gets input and validate value, returns input"""
        while True:
            try:
                user_answer = int(input(self.user_actions_menu))
                return user_answer
            except ValueError:
                print("Invalid input. Insert the number")

    def get_income(self):
        """Asks user enter income value, gets input and validate value, returns input"""
        while True:
            try:
                user_answer = int(input(self.income))
                return user_answer
            except ValueError:
                print("Invalid input. Insert the number")

    def get_transfer_card_number(self):
        """Asks user enter transfer card and returns input"""
        user_answer = input(self.transfer_card)
        return user_answer

    def get_transfer_money(self):
        """Asks user enter transfer, gets input and validate value, money and returns input"""
        while True:
            try:
                user_answer = int(input(self.transfer_money))
                return user_answer
            except ValueError:
                print("Invalid input. Insert the number")

    @classmethod
    def get_captcha(cls):
        """Generates CAPTCHA and asks user enter value and returns input"""
        InputFromUser.gen_captcha = ''.join(random.sample((string.ascii_uppercase + string.digits), 6))
        user_answer = input(f"{InputFromUser.captcha} {InputFromUser.gen_captcha}\n")
        return user_answer
