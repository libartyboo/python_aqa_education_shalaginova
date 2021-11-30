class Color:
    hex_dict = {"000000": "black", "#f44336": "red", "#2986cc": "blue"}
    message_cls = "Message from [Color Class]"

    def __init__(self, **kwargs):
        self.hex_number = kwargs.get("hex_number")

        print(f"__Init method from Color class. \n {self.__dict__}")

    def color_by_hex(self):
        print("__Func from Color class. Print color by hex")
        print(self.hex_dict[self.hex_number])

    @classmethod
    def cls_method(cls):
        print(f"__@classmethod method from Color class:")
        print(f"{cls.message_cls}")
