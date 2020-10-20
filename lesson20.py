# Магический метод __bool__
# Правдивость объектов

class Point0:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Вернёт True при любом числе, отличном от нуля
print(bool(78))
print(bool(-83.02))
print(bool(0))
print('------------------------------------------------------')

# Вернёт True если есть хотя бы один символ/элемент
print(bool('rew'))
print(bool(''))
print(bool([2, 7, 0]))
print(bool([]))
print('------------------------------------------------------')

# Всегда True, это стандартное поведение Python, чтобы изменить его, необходимо переопределить метод __bool__
p1 = Point0(1, 2)
print(f'{p1} - {bool(p1)}')
print('------------------------------------------------------')



# При отсутствии метода __bool__, интерпретатор обращается к методу __len__
class Point00:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print('__len__ called')
        return abs(self.x - self.y)

p2 = Point00(7, 12)
print(bool(p2))             # Отсутствие метода __bool__, вынуждает интерпретатор обращаться к методу __len__
print(bool(Point00(3, 9)))  # Отсутствие метода __bool__, вынуждает интерпретатор обращаться к методу __len__
print(bool(Point00(4, 4)))  # 0 даст False
print('------------------------------------------------------')



# Реализуем метод __bool__
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print('__len__ called')
        return abs(self.x - self.y)

    # Обязательно должна возвращать True или False, иначе TypeError
    def __bool__(self):
        print('__bool__ called')
        return self.x != 0 or self.y != 0

# Вызывается метод __bool_
print(bool(Point(3, 4)))        # True
print(bool(Point(-3, 0)))       # True
print(bool(Point(0, 8)))        # True
print(bool(Point(0, 0)))        # False

p3 = Point(7, 8)
# Неявный вызов метода __bool__
if p3:
    print('Hello')
print('------------------------------------------------------')
