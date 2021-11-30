"""Main module for game"""
import logging
import time
import sys
from collections import namedtuple
from input_from_players import InputFromPlayers
from game_exceptions import WinException, DrawException


class Game(InputFromPlayers):
    """
    Class for Tic Tac Toe game

    Class attributes
    ----------------
    players_order : int
    player: namedtuple
    filename: str

    Attributes
    ----------
    ** kwargs - keyword arguments:
        {'logger': obj,
        'name_1': str, 'name_2': str, 'pin_1': str, 'pin_2': str,
        'score_1': int, 'score_2': int, 'num_1': int, 'num_2': int,
        'player_1': Player(num=int, name=str, pin=str, score=int),
        'player_2': Player(num=int, name=str, pin=str, score=int)}

    """
    players_order = 0
    player = namedtuple('Player', 'num, name, pin, score')
    filename = 'game_log.log'

    def __init__(self, **kwargs):
        """
        Constructs Game object
        :param kwargs - keyword arguments:
            {'logger': obj,
            'name_1': str, 'name_2': str, 'pin_1': str, 'pin_2': str,
            'score_1': int, 'score_2': int, 'num_1': int, 'num_2': int,
            'player_1': Player(num=int, name=str, pin=str, score=int),
            'player_2': Player(num=int, name=str, pin=str, score=int)}
        """
        InputFromPlayers.__init__(self)
        self.logger = self.configure_logger()
        self.name_1 = kwargs.get("name_1")
        self.name_2 = kwargs.get("name_2")
        self.pin_1 = kwargs.get("pin_1", "X")
        self.pin_2 = kwargs.get("pin_2", "O")
        self.score_1 = kwargs.get("score_1", 0)
        self.score_2 = kwargs.get("score_2", 0)
        self.num_1 = kwargs.get("num_1", 1)
        self.num_2 = kwargs.get("num_2", 2)

        self.player_1 = self.player(num=self.num_1, name=self.name_1, pin=self.pin_1, score=self.score_1)
        self.player_2 = self.player(num=self.num_2, name=self.name_2, pin=self.pin_2, score=self.score_2)

    @property
    def print_players_info(self):
        """Prints game stats"""
        return f"'{self.player_1.name}' [X] [{self.player_1.score} : " \
               f"{self.player_2.score}] [O] '{self.player_2.name}'"

    @property
    def get_current_player_info(self):
        """Gets current active player"""
        if Game.players_order % 2 == 0:
            return self.player_1
        else:
            return self.player_2

    def set_player_name(self, player_num, name):
        """
        Sets name data
        :param player_num: int
        :param name: str
        """
        if player_num == 1:
            self.name_1 = name
            self.player_1 = self.player(num=self.num_1, name=self.name_1, pin=self.pin_1, score=self.score_1)
        else:
            self.name_2 = name
            self.player_2 = self.player(num=self.num_2, name=self.name_2, pin=self.pin_2, score=self.score_2)

    def set_player_score(self, player_num, action):
        """
        Sets score for player
        :param action: str "up" - increases score action/ "clear" - zeroes out score
        :param player_num: int
        """
        if action == "up":
            if player_num == 1:
                self.score_1 += 1
                self.player_1 = self.player(num=self.num_1, name=self.name_1, pin=self.pin_1, score=self.score_1)
            else:
                self.score_2 += 1
                self.player_2 = self.player(num=self.num_2, name=self.name_2, pin=self.pin_2, score=self.score_2)
        elif action == "clear":
            if player_num == 1:
                self.score_1 = 0
                self.player_1 = self.player(num=self.num_1, name=self.name_1, pin=self.pin_1, score=self.score_1)
            else:
                self.score_2 = 0
                self.player_2 = self.player(num=self.num_2, name=self.name_2, pin=self.pin_2, score=self.score_2)

    def configure_logger(self):
        """Configure logger for terminal and file input"""
        self.logger = logging.getLogger(__name__)

        file_handler = logging.FileHandler(self.filename)
        file_handler.setLevel(logging.WARNING)
        file_format = logging.Formatter('%(asctime)s - %(message)s')
        file_handler.setFormatter(file_format)
        self.logger.addHandler(file_handler)

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.WARNING)
        console_format = logging.Formatter('%(message)s')
        console_handler.setFormatter(console_format)
        self.logger.addHandler(console_handler)
        return self.logger

    def get_log_content(self):
        """Prints logfile content"""
        try:
            with open(self.filename, "r") as log_file:
                print(log_file.read())
        except OSError:
            self.logger.critical('File not found')
        else:
            log_file.close()

    def clear_content(self):
        """Removes logfile content"""
        try:
            with open(self.filename, "w") as log_file:
                log_file.truncate()
        except OSError:
            self.logger.critical('File not found')
        else:
            log_file.close()


    def timer(func):
        """Decorator for counting game time and displaying it in logs"""
        def wrapper(self, *args, **kwargs):
            start = time.time()
            res = func(self, *args, **kwargs)
            end = time.time()
            duration = end - start
            self.logger.warning(f'Round duration is: {duration}')
            return res
        return wrapper

    @timer
    def one_round(self):
        """
        One round logic
        """
        self.new_board()

        win = False
        while not win:
            try:
                self.print_board()
                win = self.set_xo(self.take_xo_input(self.get_current_player_info.pin),
                                  self.get_current_player_info.pin)

                if Game.players_order > 7:
                    self.print_board()
                    win = True
                    raise DrawException

                if win:
                    self.print_board()
                    self.set_player_score(self.get_current_player_info.num, action="up")
                    raise WinException(self.get_current_player_info.name)

                Game.players_order += 1
            except WinException:
                self.logger.warning(f"Player {self.get_current_player_info.name} WIN!")
            except DrawException:
                self.logger.warning("Draw!")

        Game.players_order = 0

    def game_run(self):
        """
        Continue game logic
        """
        run_game = 1
        self.logger.warning("Game Start")
        while True:
            if run_game == 1:
                self.logger.warning("New Round")
                self.one_round()
                run_game = self.continue_game()
            else:
                self.logger.warning(f"Game over. Final stats: {self.print_players_info}")
                self.set_player_score(1, action="clear")
                self.set_player_score(2, action="clear")
                break

    def main(self):
        """Runs game"""
        while True:
            menu = self.take_menu_input()
            if menu == 1:
                self.set_player_name(1, self.take_name(1))
                self.set_player_name(2, self.take_name(2))
                self.game_run()
            elif menu == 2:
                self.get_log_content()
            elif menu == 3:
                self.clear_content()
            elif menu == 4:
                print("exit")
                break


if __name__ == '__main__':
    start_game = Game()
    start_game.main()
