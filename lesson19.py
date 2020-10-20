# Магические методы __eq__ и __hash__

class Point0:
    pass


p1 = Point0()
# любое значение в Python это объект (экземпляр)
print(f'p1 is instance of Point0? - {isinstance(p1, Point0)}')
# при создании объекта в Python ему задаётся определённое поведение
print(f'Repr p1 = {p1.__repr__()}')
print(f'Hash p1 = {p1.__hash__()}')
# различные экземпляры можно сравнивать
p2 = Point0()
print(f'Hash p2 = {hash(p2)}')
print(f'p1({id(p1)}) == p2({id(p2)})? {p1 == p2}')  # False, потому что по умолчанию экземпляры сравниваются по id (адресам ячейки в памяти)
print('------------------------------------------------------------')



# Хотелось бы сравнивать объекты класса Point не по id, а по, например, координатам
class Point00:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, Point00) and self.x == other.x and self.y == other.y

p3 = Point00(1, 2)
p4 = Point00(1, 2)
# id у p3 и p4 разные, но при сравнение p3 и p4 будет результат True
print(f'id(p3) = {id(p3)}')
print(f'id(p4) = {id(p4)}')
print(f'p3({p3.x}, {p3.y}) == p4({p4.x}, {p4.y})? {p3 == p4}')
print('------------------------------------------------------------')

# Но при попытке взять hash у p3 или p4, получаем ошибку TypeError
# потому что при переопределении метода __eq__ "слетает" метод __hash__
# при переопределении метода __eq__ нужно также переопределить метод __hash__
try:
    print(hash(p3))
except TypeError as te:
    print(te)
try:
    print(hash(p4))
except TypeError as te:
    print(te)
print('------------------------------------------------------------')

# hash можно найти только у неизменяемых объектов (числа, строки, кортежи(tupple))
# т.е. все объекты делятся на hashable (хэшируемые) и unhashable(нехэшируемые)
# хэши используются в словарях (dict) в качестве ключей
d = {}
d[1] = 900              # число - неизменяемый объект (хэшируемый)
try:
    d[[3, 43]] = 900    # список(list) - изменяемый объект (нехэшируемый), выдаст ошибку TypeError
except TypeError as te:
    print(te)
# значит и точки (Point) не могут являться ключами к словарям
try:
    d[p3] = 89          # выдаст ошибку TypeError
except TypeError as te:
    print(te)
print('------------------------------------------------------------')



# Если требуется функциональность метода __hash__, его нужно переопределить
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

p5 = Point(3, 4)
p6 = Point(3, 4)
p7 = Point(30, 40)
print(f'p5({p5.x}, {p5.y}) == p6({p6.x}, {p6.y})? {p5 == p6}')
print(f'p5({p5.x}, {p5.y}) == p7({p7.x}, {p7.y})? {p5 == p7}')
print('------------------------------------------------------------')
print(f'Hash p5 = {p5.__hash__()}')
print(f'Hash p6 = {p6.__hash__()}')
print(f'Hash p7 = {p7.__hash__()}')
print('------------------------------------------------------------')

# Теперь экземпляры класса Point могут являться ключами словаря(dict)
r = {}
r[p5] = 100
print(r)
