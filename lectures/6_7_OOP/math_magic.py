class ComplexNumber:
    def __init__(self, real_part, im_part):
        self.real_part = real_part
        self.im_part = im_part

    def __str__(self):
        return f"{self.real_part} {self.im_part}j"

    def __add__(self, other):
        real = self.real_part + other.real_part
        imaginary = self.im_part + other.im_part
        print("add")
        return ComplexNumber(real, imaginary)

    def __mul__(self, other):
        real = (self.real_part * other.real_part -
                self.im_part * other.im_part)
        imaginary = (self.real_part * other.im_part +
                     other.real_part * self.im_part)
        print("mul")
        return ComplexNumber(real, imaginary)

    def __iadd__(self, other):
        self.real_part += other.real_part
        self.im_part += other.im_part
        print("iadd")
        return self

    def __eq__(self, other):
        print("equal")
        return ((self.real_part == other.real_part) and
                (self.im_part == other.im_part))


z5 = ComplexNumber(5, -5)
z6 = ComplexNumber(5, -5)
z7 = ComplexNumber(4, 4)

print(z5 + z6 + z7)

print(z5 == z6)
print(z5 == z7)

print(z5 * z6)

z5 += z7
print(z5)