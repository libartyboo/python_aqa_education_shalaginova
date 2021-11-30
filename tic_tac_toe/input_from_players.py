"""Module for inputs from players"""
from board import Board
from game_exceptions import NotCorrectValueError, AlreadyUsedValueError


class InputFromPlayers(Board):
    """Class for inputs from players"""

    @staticmethod
    def take_menu_input():
        """
        Prints Menu options string, gets input and validate value
        :return: int
        """
        while True:
            try:
                player_answer = int(input("играть - 1, просмотреть лог побед - 2, "
                                          "очистить лог побед - 3, выход - 4: "))
                return player_answer
            except ValueError:
                print("Некорректный ввод. Введите число")

    @staticmethod
    def take_name(num):
        """
        Gets player name from input
        :param num:int reflected to number of player
        :return: str
        """
        return input(f"Player [{num}]:   ")

    def take_xo_input(self, pin):
        """
        * Gets X/O position from input
        * Validate input
        :param: pin:int reflected to pin of player
        :return: int
        """
        while True:
            try:
                player_answer = int(input(f"Куда поставить {pin}? "))
                if player_answer <= 0 or player_answer >= 10:
                    raise NotCorrectValueError
                if player_answer not in self.board:
                    raise AlreadyUsedValueError
                return player_answer
            except NotCorrectValueError:
                NotCorrectValueError.error_message()
            except AlreadyUsedValueError:
                AlreadyUsedValueError.error_message()
            except ValueError:
                print("Некорректный ввод. Введите число")

    @staticmethod
    def continue_game():
        """
        Prints Continue options string, gets input and validate value
        :return: int
        """
        while True:
            try:
                player_answer = int(input("продолжить - 1, выход - 2: "))
                return player_answer
            except ValueError:
                print("Некорректный ввод. Введите число")
