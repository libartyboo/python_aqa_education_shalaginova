"""Модуль логирования и взаимодействия с файлом логов"""
import logging
import time
import sys


class GameLogger:
    """Класс логирования и взаимодействия с файлом логов"""
    filename = 'game_log.log'

    def __init__(self):
        """Создание логера по заданной конфигурации"""
        self.logger = self.configure_logger()

    def configure_logger(self):
        """Конфигурация логера"""
        self.logger = logging.getLogger(__name__)

        file_handler = logging.FileHandler(GameLogger.filename)
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
        """Метод выводит содержимое лог фала в терминал"""
        try:
            with open(GameLogger.filename, "r") as log_file:
                print(log_file.read())
        except OSError:
            self.logger.critical('File not found')
        else:
            log_file.close()

    def clear_content(self):
        """Метод очищает лог файл"""
        try:
            with open(GameLogger.filename, "w") as log_file:
                log_file.truncate()
        except OSError:
            self.logger.critical('File not found')
        else:
            log_file.close()

    @staticmethod
    def timer(func):
        """Декоратор для подсчета времени игры и его вывода в логах"""
        def wrapper(self, *args, **kwargs):
            start = time.time()
            res = func(self, *args, **kwargs)
            end = time.time()
            duration = end - start
            self.logger.warning(f'Set duration is: {duration}')
            return res

        return wrapper
