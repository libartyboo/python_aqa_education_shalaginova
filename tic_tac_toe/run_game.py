"""Runs game out of Game class"""
from game import Game

while True:
    try:
        menu = int(input("играть - 1, просмотреть лог побед - 2, "
                         "очистить лог побед - 3, выход - 4: "))
        if menu == 1:
            player_1 = input("Player [1]:   ")
            player_2 = input("Player [2]:   ")
            start_game = Game(name_1=player_1, name_2=player_2)
            start_game.game_run()
        elif menu == 2:
            get_log = Game()
            get_log.get_log_content()
        elif menu == 3:
            get_log = Game()
            get_log.clear_content()
        else:
            print("exit")
            break
    except ValueError:
        print("Некорректный ввод. Введите число")
