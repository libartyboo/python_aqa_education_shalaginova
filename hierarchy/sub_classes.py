from transport import Transport
from color import Color
from user_actions import UserActions


class Road(Transport):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.transport_type = kwargs.get("transport_type", "Road")
        self.road_transport_type = kwargs.get("road_transport_type")

        print(f"__Init method from Road(Transport) class. \nObject [{self.n}]: {self.__dict__}")

    def start(self):
        print("__Abstract method from Transport")
        return f"{self.transport_type} start ride"


class Rail(Transport):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.passengers = kwargs.get("passengers")

        print(f"__Init method from Rail(Transport) class. \nObject [{self.n}]: {self.__dict__}")

    def __str__(self):
        print(f"__Str method from Rail(Transport) class:")
        print_str = f"{self.rail_description()}. {self.max_speed()}"
        return print_str

    def rail_description(self):
        return f"The {self.transport_type} transport can take {self.passengers} passengers"

    def rail_message(self):
        print("__Func from Rail(Transport) which call @classmethod and print(self)")
        super().cls_method()
        print(self)

    def start(self):
        print("__Abstract method from Transport")
        return f"{self.transport_type} start ride"


class Air(Transport):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pilot_num = kwargs.get("pilot_num")
        self.passengers = kwargs.get("passengers")

        print(f"__Init method from Air(Transport) class. \nObject [{self.n}]: {self.__dict__}")

    def __str__(self):
        print(f"__Str method from Air(Transport) class:")
        print_str = f"{self.air_description()}"
        return print_str

    def air_description(self):
        return f"The {self.transport_type} transport can FLY with {self.pilot_num} pilots " \
               f"and take {self.passengers} passengers"

    @property
    def fly_info(self):
        print("__@proprty method from Air(Transport) class")
        return f"{self.transport_type} transport type | {self.pilot_num} pilots | {self.passengers} passengers"

    def start(self):
        print("__Abstract method from Transport")
        return f"{self.transport_type} start ride"


class Water(Transport, Color):

    def __init__(self, **kwargs):
        Transport.__init__(self, **kwargs)
        Color.__init__(self, **kwargs)
        self.water_proof = kwargs.get("water_proof")

        print(f"__Init method from Water(Transport, Color) class. \nObject [{self.n}]: {self.__dict__}")
        print(f"__MRO order: \n {Water.__mro__}")

    def start(self):
        print("__Abstract method from Transport")
        return f"{self.transport_type} start ride"


class Space(Color, Transport):

    def __init__(self, **kwargs):
        Color.__init__(self, **kwargs)
        Transport.__init__(self, **kwargs)

        print(f"__Init method from Space(Color, Transport) class. \nObject [{self.n}]: {self.__dict__}")
        print(f"__MRO order: \n {Space.__mro__}")

    def start(self):
        print("__Abstract method from Transport")
        return f"{self.transport_type} start ride"


class Bike(Transport, Color, UserActions):

    def __init__(self, **kwargs):
        Transport.__init__(self, **kwargs)
        Color.__init__(self, **kwargs)
        UserActions.__init__(self, **kwargs)
        self.bike_string = kwargs.get("bike_string")
        self.carrying_capacity = 0

        print(f"__Init method from Bike(Transport, Color, UserActions) class. \nObject [{self.n}]: {self.__dict__}")

    def turn_right(self):
        print("__Abstract method from UserActions class")
        return f"{self.first_name} {self.last_name} {self.driver_data} turn right"

    def turn_left(self):
        print("__Abstract method from UserActions class")
        return f"{self.first_name} {self.last_name} {self.driver_data} turn left"

    def start(self):
        print("__Abstract method from Transport and UserActions classes")
        return f"{self.first_name} {self.last_name} {self.driver_data} start ride"
