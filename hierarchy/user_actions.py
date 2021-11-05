from abc import ABC, abstractmethod


class UserActions(ABC):
    def __init__(self, **kwargs):
        self.first_name = kwargs.get("first_name")
        self.last_name = kwargs.get("last_name")
        self.driver_data = kwargs.get("driver_data")

    @abstractmethod
    def start(self):
        ...

    @abstractmethod
    def turn_left(self):
        ...

    @abstractmethod
    def turn_right(self):
        ...
