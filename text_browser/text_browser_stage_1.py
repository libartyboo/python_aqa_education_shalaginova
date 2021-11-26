class TextBrowserS1:
    __BLOOMBERG = '''The Space Race: From Apollo 11 to Elon Musk

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
Tuesday, a signal of the strong ties between the Silicon Valley giants.'''

    __NATIMES = '''This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow
and change shape, and that could be a boon to medicine
and robotics. (Source: New York Times)

Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
important female and minority scientists in less than two
years.'''
    __URLS = {"bloomberg.com": __BLOOMBERG, "nytimes.com": __NATIMES}
    __MAIN_MENU = '''bloomberg.com OR nytimes.com
exit'''
    __WRONG_INPUT = "Wrong input. Try again!"

    def __init__(self):
        self.state = "open"
        self.urls = self.__URLS

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
        return url in self.urls.keys()

    def open_url(self, url):
        print(self.urls[url])
        return self.__MAIN_MENU


if __name__ == '__main__':
    tb = TextBrowserS1()
    response = tb.start()
    while True:
        user_input = input(response + "\n")
        response = tb.take_url(user_input)
        if tb.state == "closed":
            break
