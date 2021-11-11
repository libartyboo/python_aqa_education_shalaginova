from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, name, rank, level):
        self.name = name
        self.rank = rank
        self.level = level
        super().__init__()

    @abstractmethod
    def fight(self):
        ...

    @abstractmethod
    def do_spell(self):
        ...

    def sing_song(self):
        print("No songs for me!")


class Bard(Player):
    def fight(self):
        print("Smash the opponent with your lute.")

    def do_spell(self):
        print("Increase weapon fatality")

    def sing_song(self):
        print("Sing a beautiful song.")


class Warrior(Player):
    def fight(self):
        print("Swing an ax")

    def do_spell(self):
        print("Increase weapon fatality")


bard = Bard("Jaskier", 4, 5)
bard.fight()
bard.do_spell()
bard.sing_song()

warrior = Warrior("Bran", 1, 1)
warrior.fight()
warrior.do_spell()
warrior.sing_song()


class USB(ABC):

    @abstractmethod
    def charge(self):
        ...

    @abstractmethod
    def transfer(self):
        ...


class HDMI(ABC):

    @abstractmethod
    def show(self):
        ...


class Laptop(USB, HDMI):
    def charge(self):
        print("Charging...")

    def transfer(self):
        print("Transferring data...")

    def show(self):
        print("Showing...")


laptop = Laptop()
laptop.charge()
laptop.transfer()
laptop.show()

print(isinstance(laptop, USB))
print(isinstance(laptop, HDMI))


def my_fun(notebook: USB) -> str:
    notebook.charge()
    return "fgdfg"


f = int(input())
print(f)
