"""Module for exceptions"""


class NotCorrectValueError(Exception):
    @staticmethod
    def error_message():
        print("Некорректный ввод. Введите число в игровом диапазоне от 1 до 9")


class AlreadyUsedValueError(Exception):
    @staticmethod
    def error_message():
        print("Некорректный ввод. Клетка занята")


class WinException(Exception):
    def __init__(self, player):
        self.player = player

    @property
    def player_name(self):
        return self.player


class DrawException(Exception):
    ...
