class Phone:

    def __init__(self, *args, **kwargs):
        if kwargs:
            self.screen = kwargs['screen']
            self.memory = kwargs["memory"]
            self.model = kwargs["model"]
            self.vendor = kwargs['vendor']
        else:
            self.screen = args[0]
            self.memory = args[1]
            self.model = args[2]
            self.vendor = args[3]


phone = Phone(memory=4, screen=5.7, model='A4', vendor='LG',)
print(phone.screen)
print(phone.vendor)
print(phone.memory)
print(phone.__dict__)

phone1 = Phone(6.5, 3, 'Galaxy', 'Samsung')
print(phone1.screen)
print(phone1.vendor)
print(phone1.memory)
print(phone1.__dict__)


class IPhone(Phone):
    # TODO - create some fields and methods
    ...


iphone = IPhone(4.7, 16, '6S', 'Apple')
print(iphone.screen)
print(iphone.memory)


class Player:

    def __init__(self, play_format='mp3'):
        self.play_format = play_format

    def play_music(self):
        print(f"Play music in format {self.play_format}")


class Android(Phone, Player):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        super(Player, self).__init__()
        if kwargs:
            self.screen_height = kwargs['screen_height']
            self.screen_width = kwargs['screen_width']
            self.version = kwargs.get('version', 11)

        elif args:
            self.screen_height = args[4]
            self.screen_width = args[5]
            self.version = None


android = Android(memory=4, screen=5.7, model='A4', vendor='LG',
                  screen_width=2, screen_height=3.5, version=11)
print(android.memory)

android1 = Android(4.7, 16, '6S', 'Apple', 2, 3.5, 11)
print(android1.play_format)

android1.play_music()
