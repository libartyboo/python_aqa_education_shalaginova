"""Модуль создания игроков"""
from collections import namedtuple


class Players:
    """Модуль создания игроков"""
    player = namedtuple('Player', 'num, name, pin, score')

    def __init__(self, **kwargs):
        self.name_1 = kwargs.get("name_1")
        self.name_2 = kwargs.get("name_2")
        self.pin_1 = kwargs.get("pin_1", "X")
        self.pin_2 = kwargs.get("pin_2", "O")
        self.score_1 = kwargs.get("score_1", 0)
        self.score_2 = kwargs.get("score_2", 0)
        self.num_1 = kwargs.get("num_1", 1)
        self.num_2 = kwargs.get("num_2", 2)

        self.player_1 = Players.player\
            (num=self.num_1, name=self.name_1, pin=self.pin_1, score=self.score_1)
        self.player_2 = Players.player\
            (num=self.num_2, name=self.name_2, pin=self.pin_2, score=self.score_2)

    @property
    def print_players_info(self):
        """Метод выводит статистику игры - имена и счет"""
        return f"'{self.player_1.name}' [X] [{self.player_1.score} : " \
               f"{self.player_2.score}] [O] '{self.player_2.name}'"
