import sys
import os
import os.path
import requests
from urllib.parse import urlparse
from collections import deque


class TextBrowserS4:
    __MAIN_MENU = "enter URL | exit"
    __MAIN_MENU_BACK = "back | enter URL | exit"
    __WRONG_INPUT = "Error: Incorrect URL"

    def __init__(self):
        self.dir_name = self.dir_name()
        self.create_folder()
        self.state = "open"
        self.history = deque()
        self.url = None

    @staticmethod
    def dir_name():
        if len(sys.argv) > 1:
            return sys.argv[1]
        else:
            return "dir-for-files"

    def create_folder(self):
        try:
            if os.access(self.dir_name, os.F_OK):
                raise FileExistsError
            else:
                os.makedirs(self.dir_name)
        except FileExistsError:
            ...

    def main_menu(self):
        if len(self.history) >= 2:
            return self.__MAIN_MENU_BACK
        else:
            return self.__MAIN_MENU

    def start(self):
        return self.main_menu()

    def take_url(self, url):
        if self.check_user_input(url):
            return self.open_url(self.url)
        elif url == "exit":
            self.state = "closed"
            return self.state
        elif url == "back":
            return self.back()
        else:
            return self.__WRONG_INPUT

    def check_user_input(self, url):
        url = urlparse(url)
        try:
            if not url.scheme:
                url = urlparse("https://" + url.geturl())
            if url.netloc.find('.') < 1:
                raise ValueError
            self.url = url.geturl()
            return True
        except ValueError:
            return False

    def open_url(self, url):
        r = requests.get(url)
        print(r.text)
        self.save_url_content(url, r.text)
        self.history.append(url)
        return self.main_menu()

    @staticmethod
    def parse_file_name(url):
        url = urlparse(url)
        return url.netloc.replace(".", "") + url.path.replace("/", "_")

    def save_url_content(self, url, content):
        file_path = os.path.join(self.dir_name, self.parse_file_name(url))
        with open(file_path, "a+", encoding='utf-8') as url_file:
            url_file.write(content)
            url_file.close()

    def back(self):
        if len(self.history) >= 2:
            self.history.pop()
            url = self.history.pop()
            self.open_url(url)
        return self.main_menu()


if __name__ == '__main__':
    tb = TextBrowserS4()
    response = tb.start()
    while True:
        user_input = input(response + "\n")
        response = tb.take_url(user_input)
        if tb.state == "closed":
            break
