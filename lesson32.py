# Slots Слоты
from timeit import timeit

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y



p1 = Point(2, 3)
print(p1.x, p1.y)                   # к какждому атрибуту можем обратиться через точку '.'
print(p1.__dict__)

p1.q = 100                          # динамическое создание атрибута
print(p1.q)
print(p1.__dict__)
print('------------------------------------------------------------------')

# Как ограничить количество/имена атрибутов в классе?

class PointSlots:

    # Укажем какие атрибуты будут использованы в классе в виде кортежа (tupple)
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


p2 = PointSlots(3, 4)
print(p2.x, p2.y)                   # обращаться через точку всё ещё можно
try:
    print(p2.__dict__)              # вызовет ошибку AttributeError
except AttributeError as ae:
    print(ae)

p2.y = 12                           # мы по-прежнему можем изменять атрибуты
del p2.y                            # и удалять их

try:
    p2.q = 200                      # но мы не можем добавлять новые атрибуты
except AttributeError as ae:
    print(ae)

print('------------------------------------------------------------------')

# При использовании __slots__ объекты занимают меньше памяти
s = Point(45, 78)
print(s.__sizeof__(), s.__dict__.__sizeof__())  # __dict__ занимает дополнительное место в памяти
d = PointSlots(21, 90)
print(d.__sizeof__())

print('------------------------------------------------------------------')

# и "выполняются"(создаются) быстрее
def make_cl1():
    s = Point(7, 2)
    s.x = 100
    s.x
    del s.x

def make_cl2():
    s = PointSlots(1, 0)
    s.x = 200
    s.x
    del s.x

print(timeit(make_cl1))
print(timeit(make_cl2))
