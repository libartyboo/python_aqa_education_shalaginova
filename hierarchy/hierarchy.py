from sub_classes import Road, Rail, Air, Water, Space, Bike
from transport import Transport

print("------------------------------------------------------------------------------")
# Road(Transport) class
# __str__ and get @property from Transport class
transport_1 = Road(speed=200, carrying_capacity=300, road_transport_type="basic car")
print(transport_1)
print(transport_1.property_from_transport)

#
print("------------------------------------------------------------------------------")
# Rail(Transport) class
# Func from Rail(Transport) which call Transport @classmethod and print(self)
transport_2 = Rail(transport_type="Rail", speed=100, passengers=1000)
transport_2.rail_message()

print("------------------------------------------------------------------------------")
# Air(Transport) class
# __str__ and @proprty from Air(Transport) class
transport_3 = Air(transport_type="Air", speed=987, pilot_num=2, passengers=100)
print(transport_3)
print(transport_3.fly_info)

print("------------------------------------------------------------------------------")
# Water(Transport, Color) class
# MRO order
transport_4 = Water(transport_type="Water", speed=150, water_proof=1999, carrying_capacity=15, hex_number="000000")
transport_4.color_by_hex()
print(transport_4.property_from_transport)
transport_4.cls_method()

print("------------------------------------------------------------------------------")
# Space(Color, Transport) class
# MRO order
transport_5 = Space(transport_type="Space", speed=111111, carrying_capacity=10, hex_number="#f44336")
transport_5.color_by_hex()
transport_5.cls_method()

print("------------------------------------------------------------------------------")
# Bike(Transport, Color, UserActions) class
# @staticmethod from Transport
# @abstractmethod from Transport and UserActions
# func from Color
transport_6 = Bike(transport_type="Bike", speed=40, hex_number="#2986cc")
transport_6.bike_string = transport_6.gen_method()
transport_6.first_name = "John"
transport_6.last_name = "Doe"
transport_6.driver_data = "Qw123R45Ty123"
print(f"Object [{transport_6.n}]: {transport_6.__dict__}")
transport_6.color_by_hex()
print(transport_6.start())
print(transport_6.turn_left())
print(transport_6.turn_right())

print("------------------------------------------------------------------------------")
# Magic methods
# __repr__
Transport.__repr__(Transport)
# __gt__
if transport_1 > transport_2:
    print(f"\n{transport_1.transport_type} transport more powerful then {transport_2.transport_type} transport")
# __lt__
if transport_2 < transport_3:
    print(f"\n{transport_2.transport_type} transport less powerful then {transport_3.transport_type} transport")
# __ge__
if transport_4 >= transport_5:
    print(f"\n{len(transport_4.__dict__)} >= {len(transport_5.__dict__)}")
# __le__
if transport_5 <= transport_6:
    print(f"\n{len(transport_5.__dict__)} <= {len(transport_6.__dict__)}")
# __eq__
if transport_1.transport_type == Transport.transports[1]["transport_type"]:
    print(f"\nObject attr in the list")
# __ne__
if transport_2.transport_type != transport_1.transport_type:
    print(f"\nObjects are different\n")
# __add__
print(transport_1 + transport_2)
print(transport_2 + transport_3)
