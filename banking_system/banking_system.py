"""Banking System"""
import time
from input_from_user import InputFromUser
from card_number import generate_card, generate_password, luhn
from db import BankingDB
from banking_sys_exceptions import NotExistCardException, NotEnoughMoneyException, \
    OwnCardException, AuthException, LuhnException


class BankingSystem(InputFromUser, BankingDB):
    """
    Class for BankingSystem

    Class attributes
    ----------------
    __LOGIN_ATTEMPTS : int
    __ATTEMPTS : int
    __BLOCKING_TIME : date, None by default
    __BLOCKING_DURATION : int
    __CAPTCHA : boolean, False by default

    Attributes
    ----------
    user_id: int, None by default

    """
    __LOGIN_ATTEMPTS = 0
    __ATTEMPTS = 5
    __BLOCKING_TIME = None
    __BLOCKING_DURATION = 60
    __CAPTCHA = False

    def __init__(self):
        BankingDB.__init__(self)
        self.user_id = None

    def create_account(self):
        """Creates new account"""
        card = generate_card()
        pin = generate_password()
        self.db_create_account(card, pin)
        print(f"Your card has been created"
              f"\nYour card number:"
              f"\n{card}"
              f"\nYour card PIN:"
              f"\n{pin}")

    def login(self, brute_force_check=False):
        """
        Login feature:
        * Gets user input (card and pin)
        * Checks card by LUHN
        * Checks data in db
         * Prints 'auth' validate message if card value not valid by LUHN check
         * Prints 'auth' validate message if user doesn't exist in db
         * Prints 'success' message, sets self.user_id and runs user_actions() method

        Avoids Brute Force attack:
        * Provides unspecified message in failed login case
        * Blocks Login after __ATTEMPTS value failed attempts
        * Blocking time is __BLOCKING_DURATION
        * Captcha should be solved to enable Login

        :param brute_force_check: boolean, False by default
        :return: None
        """
        BankingSystem.check_blocking_time()
        if BankingSystem.__LOGIN_ATTEMPTS < BankingSystem.__ATTEMPTS:
            if not BankingSystem.__CAPTCHA:
                if not brute_force_check:
                    login_card = self.login_get_card_number()
                    login_pin = self.login_get_pin()
                else:
                    login_card = generate_card()
                    login_pin = generate_password()
                    print(f"login > card: {login_card}, pin: {login_pin}")

                try:
                    if not luhn(login_card):
                        raise LuhnException
                    user_id = self.db_select_userid(login_card, login_pin)
                    if user_id:
                        self.user_id = user_id[0]
                        print("You have successfully logged in!")
                        self.user_actions()
                    else:
                        raise AuthException
                except (LuhnException, AuthException):
                    BankingSystem.__LOGIN_ATTEMPTS += 1
                    if BankingSystem.__LOGIN_ATTEMPTS == BankingSystem.__ATTEMPTS:
                        BankingSystem.__BLOCKING_TIME = time.time()
                    print("Wrong CARD or PIN!")
            else:
                BankingSystem.check_captcha()
        else:
            print("Login feature has been blocked for a while. Try again later!")

    @classmethod
    def check_blocking_time(cls):
        """Checks blocking time. Turn on CAPTCHA validation"""
        if BankingSystem.__BLOCKING_TIME:
            current_time = time.time()
            if current_time - BankingSystem.__BLOCKING_TIME > BankingSystem.__BLOCKING_DURATION:
                BankingSystem.__BLOCKING_TIME = None
                BankingSystem.__LOGIN_ATTEMPTS = 0
                BankingSystem.__CAPTCHA = True

    @classmethod
    def check_captcha(cls):
        """Checks CAPTCHA from user and turns off CAPTCHA validation if pass"""
        user_captcha = InputFromUser.get_captcha()
        if BankingSystem.gen_captcha == user_captcha:
            BankingSystem.__CAPTCHA = False
            print("That's all. You're not a robot!")
        else:
            print("Wrong CAPTCHA!")

    def logout(self):
        """Sets None in self.user_id"""
        self.user_id = None

    def money_transfer(self):
        """
        Transfers money from user to another
        * Gets transfer card and validates card by LUHN. Prints error message if card doesn't valid
        * Prints error message if user try to transfer money to own card
        * Prints error message if user doesn't have enough money
        * Prints error message if transfer card doesn't exist in db
        * Transfers money if all validations passed
        """
        transfer_card = self.get_transfer_card_number()
        if luhn(transfer_card):
            transfer_id = self.db_select_transfer_id(transfer_card)
            try:
                if transfer_id:
                    if transfer_id[0] == self.user_id:
                        raise OwnCardException
                else:
                    raise NotExistCardException

                transfer_money = self.get_transfer_money()

                if transfer_money > self.db_select_user_balance(self.user_id)[0]:
                    raise NotEnoughMoneyException

                self.db_transfer_money(self.user_id, transfer_id[0], transfer_money)
                print("Success!")
            except NotExistCardException:
                NotExistCardException.error_message()
            except NotEnoughMoneyException:
                NotEnoughMoneyException.error_message()
            except OwnCardException:
                OwnCardException.error_message()
        else:
            print("Probably you made a mistake in the card number. Please try again!")

    def user_actions(self):
        """Prints user actions for loggedin user"""
        while True:
            user_action = self.get_user_actions()
            if user_action == 1:
                print(self.db_select_user_balance(self.user_id)[0])
            elif user_action == 2:
                self.db_update_user_balance(self.user_id, self.get_income())
                print("Income was added!")
            elif user_action == 3:
                self.money_transfer()
            elif user_action == 4:
                self.db_delete_account(self.user_id)
                self.logout()
                print("The account has been closed!")
                break
            elif user_action == 5:
                self.logout()
                print("You have successfully logged out!")
                break
            elif user_action == 0:
                self.logout()
                break

    def main(self):
        """Prints Banking menu"""
        while True:
            menu = self.get_menu_item()
            if menu == 1:
                self.create_account()
            if menu == 2:
                self.login()
            elif menu == 0:
                print("Bye!")
                break


if __name__ == '__main__':
    banking_system = BankingSystem()
    banking_system.main()
