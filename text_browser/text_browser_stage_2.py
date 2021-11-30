import time
import sys
import os
import os.path
import re
from urllib.parse import urlparse


class TextBrowserS2:
    __BLOOMBERG = '''
    The Space Race: From Apollo 11 to Elon Musk

    It's 50 years since the world was gripped by historic images
    of Apollo 11, and Neil Armstrong -- the first man to walk
    on the moon. It was the height of the Cold War, and the charts
    were filled with David Bowie's Space Oddity, and Creedence's
    Bad Moon Rising. The world is a very different place than
    it was 5 decades ago. But how has the space race changed since
    the summer of '69? (Source: Bloomberg)

    Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

    Twitter and Square Chief Executive Officer Jack Dorsey
    addressed Apple Inc. employees at the iPhone maker’s headquarters
    Tuesday, a signal of the strong ties between the Silicon Valley giants.
    '''

    __NATIMES = '''
    This New Liquid Is Magnetic, and Mesmerizing

    Scientists have created “soft” magnets that can flow
    and change shape, and that could be a boon to medicine
    and robotics. (Source: New York Times)

    Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

    Jessica Wade has added nearly 700 Wikipedia biographies for
    important female and minority scientists in less than two
    years.
    '''
    __URLS = {"bloomberg.com": __BLOOMBERG, "nytimes.com": __NATIMES}
    __MAIN_MENU = '''bloomberg.com OR nytimes.com
exit'''
    __WRONG_INPUT = "Error: Incorrect URL"

    def __init__(self):
        self.dir_name = self.dir_name()
        self.create_folder()
        self.state = "open"
        self.urls = self.__URLS

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

    def start(self):
        return self.__MAIN_MENU

    def take_url(self, url):
        if self.check_user_input(url):
            return self.open_url(url)
        elif url == "exit":
            self.state = "closed"
            return self.state
        else:
            return self.__WRONG_INPUT

    def check_user_input(self, url):
        url = urlparse(url)
        try:
            if re.findall('.', str(url.port)):
                return url.geturl() in self.urls.keys()
            else:
                raise ValueError
        except ValueError:
            return False

    def open_url(self, url):
        self.save_url_content(url)
        print(self.urls[url])
        return self.__MAIN_MENU

    def save_url_content(self, url):
        file_path = os.path.join(self.dir_name, re.findall(r'([^.]*)', url)[0])
        with open(file_path, "w") as url_file:
            url_file.write(self.urls[url])
            url_file.close()


if __name__ == '__main__':
    tb = TextBrowserS2()
    response = tb.start()
    while True:
        user_input = input(response + "\n")
        response = tb.take_url(user_input)
        if tb.state == "closed":
            break
