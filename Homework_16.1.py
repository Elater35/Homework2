# ДЗ 16.1. Клас "Прямокутник"

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def get_sides_from_square(self, other, square):
        if max(self.width, other.width) >= 1:
            new_width = int(max(self.width, other.width))
            new_width = new_width if new_width % 2 == 0 else new_width + 1
        else:
            new_width = 1
        new_height = square / new_width
        return Rectangle(new_width, new_height)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.get_square() == other.get_square()

    def __add__(self, other):
        if isinstance(other, Rectangle):
            square = self.get_square() + other.get_square()
            new_rectangle = self.get_sides_from_square(other, square)
            return new_rectangle

    def __mul__(self, multiplier):
        square = self.get_square() * multiplier
        new_rectangle = self.get_sides_from_square(Rectangle(1,1), square)
        return new_rectangle

    def __str__(self):
        return f"Rectangle with width {self.width} and height {self.height}"


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'
