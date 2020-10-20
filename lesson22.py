# Полиморфизм
from math import pi

class Rectangle:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_rect_area(self):
        return self.a * self.b

    def get_area(self):
        return self.a * self.b

    def __str__(self):
        return f'Rectangle {self.a}x{self.b}'

class Square:

    def __init__(self, a):
        self.a = a

    def get_sq_area(self):
        return self.a ** 2

    def get_area(self):
        return self.a ** 2

    def __str__(self):
        return f'Square {self.a}x{self.a}'

class Circle:
    def __init__(self, r):
        self.r = r

    def get_circle_area(self):
        return (self.r ** 2) * pi

    def get_area(self):
        return (self.r ** 2) * pi

    def __str__(self):
        return f'Circle radius={self.r}'
