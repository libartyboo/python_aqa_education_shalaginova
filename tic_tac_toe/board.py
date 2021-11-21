"""Module for game board"""


class Board:
    """Class for creating, printing and modifying Game Board object"""

    def __init__(self):
        """
        Constructs Game Board object

        Attributes:
        board: predefined list of integers from 1 to 9
        win_combinations: predefined nested list of win combinations
        """
        self.board = [i for i in range(1, 10)]
        self.win_combinations = [[1, 2, 3],
                                 [4, 5, 6],
                                 [7, 8, 9],
                                 [1, 4, 7],
                                 [2, 5, 8],
                                 [3, 6, 9],
                                 [1, 5, 9],
                                 [7, 5, 3]]

    def new_board(self):
        """Updates Game Board attributes to default values"""
        self.board = [i for i in range(1, 10)]
        self.win_combinations = [[1, 2, 3],
                                 [4, 5, 6],
                                 [7, 8, 9],
                                 [1, 4, 7],
                                 [2, 5, 8],
                                 [3, 6, 9],
                                 [1, 5, 9],
                                 [7, 5, 3]]

    def print_board(self):
        """Prints formatted "board" list in terminal"""
        for i in range(3):
            k = i * 3
            print(*self.board[k:k + 3], sep=" | ")

    def set_xo(self, position, pin):
        """
        - Modifies board and win_combinations lists by player position and pin
        - Checks win combination
        :param position:int
        :param pin:str
        :return: True if win combination contain 3 the same pins from active player
        """
        self.board[position - 1] = pin

        for combination in self.win_combinations:
            index_first = self.win_combinations.index(combination)
            for _ in combination:
                if position in combination:
                    index_second = combination.index(int(position))
                    self.win_combinations[index_first][index_second] = pin
            if combination == [pin]*3:
                return True
