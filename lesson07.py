# Практика. Класс Point
from math import sqrt

class Point:

    list_points = []

    # Метод написания кода DRY (Don't Repeat Yourself)
    def __init__(self, coord_x = 0, coord_y = 0):
        self.x = coord_x
        self.y = coord_y
        Point.list_points.append(self)              # Отразится на всех экземплярах класса Point

    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def go_home(self):
        self.move_to(0, 0)

    def print_point(self):
        print(f"Точка с координатами ({self.x}, {self.y})")

    def calc_distance(self, another_point):
        if not isinstance(another_point, Point):
            raise ValueError("Аргумент должен принадлежать классу Point")
        return sqrt((self.x - another_point.x) ** 2 + (self.y - another_point.y) ** 2)



p1 = Point(3, 4)
print([p1.x, p1.y])
p2 = Point(-54, 32)
print([p2.x, p2.y])
p3 = Point()            # Выдаст ошибку TypeError, если аргументы метода __init__ обязательны
print([p3.x, p3.y])
print(Point.list_points)
print()

p3.move_to(4, 5)
print([p3.x, p3.y])
p3.move_to(-90, 5)
print([p3.x, p3.y])
print(Point.list_points)
print()

p4 = Point(4)
print([p4.x, p4.y])
p4.move_to(4, 8)
print([p4.x, p4.y])
p4.move_to(8, 8)
print([p4.x, p4.y])
p4.go_home()
print([p4.x, p4.y])
print(Point.list_points)
print()

p5 = Point()
p5.print_point()
p5.move_to(7, -43)
p5.print_point()
print(Point.list_points)
print()

p7 = Point(6, 0)
p8 = Point(0, 8)
#p7.calc_distance(90)       # Вызовет исключение ValueError
print(p7.calc_distance(p8))
print(Point.list_points)
print(Point.list_points[2])
print('y = ' + str(Point.list_points[2].y))
print()

print(p7.list_points)
