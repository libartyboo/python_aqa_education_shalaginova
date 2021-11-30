from abc import ABC, abstractmethod


class Transport(ABC):
    message_cls = 'Message from [Transport Class]'
    transports = {}
    n = 0

    def __new__(cls, **kwargs):
        print("\n__New method from Transport class. Object is created")
        return object.__new__(cls)

    def __init__(self, **kwargs):
        self.transport_type = kwargs.get("transport_type")
        self.speed = kwargs.get("speed")
        self.carrying_capacity = kwargs.get("carrying_capacity")

        Transport.n += 1
        Transport.transports[Transport.n] = self.__dict__

        print(f"__Init method from Transport class. \nObject [{self.n}]: {self.__dict__}")

    def __str__(self):
        print(f"__Str method from Transport class")
        print_str = f"{self.description()}. {self.max_speed()}"
        return print_str

    def __repr__(self):
        for key in Transport.transports:
            print(f"Object [{key}]: {Transport.transports[key]}")
        return repr(self)

    @abstractmethod
    def start(self):
        ...

    @classmethod
    def cls_method(cls):
        print(f"__@classmethod method from Transport class:")
        print(f"{cls.message_cls}")

    def description(self):
        return f"The {self.transport_type} transport can take {self.carrying_capacity} kg"

    def max_speed(self):
        return f"The {self.transport_type} transport runs at the maximum speed of {self.speed * 2} km/hr"

    @staticmethod
    def gen_method():
        return "Static"

    @property
    def property_from_transport(self):
        print("__@proprty method from Transport class")
        return f"{self.n * 2 ** 3}"

    def __gt__(self, other):
        values_gt = {"speed_1": self.speed,
                     "speed_2": other.speed,
                     "carrying_capacity_1": self.carrying_capacity,
                     "carrying_capacity_2": other.carrying_capacity}
        for key in values_gt:
            if values_gt[key] is None:
                values_gt[key] = 0

        val_1 = values_gt["speed_1"]
        val_2 = values_gt["speed_2"]

        if values_gt["carrying_capacity_1"] > 0:
            val_1 = values_gt["speed_1"] * 1.2
        elif values_gt["carrying_capacity_2"] > 0:
            val_2 = values_gt["speed_2"] * 1.2
        return val_1 > val_2

    def __lt__(self, other):
        values_gt = {"speed_1": self.speed,
                     "speed_2": other.speed,
                     "carrying_capacity_1": self.carrying_capacity,
                     "carrying_capacity_2": other.carrying_capacity}
        for key in values_gt:
            if values_gt[key] is None:
                values_gt[key] = 0

        val_1 = values_gt["speed_1"]
        val_2 = values_gt["speed_2"]

        if values_gt["carrying_capacity_1"] > 0:
            val_1 = values_gt["speed_1"] * 1.2
        elif values_gt["carrying_capacity_2"] > 0:
            val_2 = values_gt["speed_2"] * 1.2
        return val_1 < val_2

    def __ge__(self, other):
        return len(self.__dict__) >= len(other.__dict__)

    def __le__(self, other):
        return len(self.__dict__) <= len(other.__dict__)

    def __eq__(self, other):
        return self.transport_type == other.transport_type

    def __ne__(self, other):
        return self.transport_type != other.transport_type

    def __add__(self, other):
        speed = self.speed + other.speed
        transport_type = self.transport_type + ' and ' + other.transport_type + ' speed'
        return transport_type, speed

