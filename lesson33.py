# Slots, property и наследование

class Rectangle:
    __slots__ = 'width', 'height'

    def __init__(self, a, b):
        self.width = a
        self.height = b

    @property
    def perimetr(self):
        return (self.height + self.width) * 2

    @property
    def area(self):
        return self.height * self.width



a = Rectangle(3, 4)
print(f'a = {a.width}')
print(f'b = {a.height}')
try:
    a.zz = 100
except AttributeError as ae:
    print(ae)
print('--------------------------------------------------------------------')

b = Rectangle(4, 5)
# area и perimetr не присутствуют в __slots__, однако не вызывают ошибку, потому что являются не атрибутами,
# а задекорированными методами
print(f'S = {b.area}')
print(f'P = {b.perimetr}')
print('--------------------------------------------------------------------')

#-------------------------------------------------------------------------------

class Rectangle:
    __slots__ = '__width', 'height'

    def __init__(self, a, b):
        self.width = a
        self.height = b

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w):
        print('setter called')
        self.__width = w

c = Rectangle(5, 6)
print(c.width)
print(c._Rectangle__width)
print('--------------------------------------------------------------------')

#-------------------------------------------------------------------------------

class Square(Rectangle):
    pass
# Экземпляры дочерних классов будут иметь переменную __dict__ несмотря на наличие __slots__ у родительского класса.
# Значит в экземпляры дочерних классов мы можем присваивать любые атрибуты
s = Square(7, 8)
print(s.__dict__)
s.zz = 100
print(s.zz)
print('--------------------------------------------------------------------')

#-------------------------------------------------------------------------------

# В дочерних классах тоже можно определить перечень __slots__
class Square(Rectangle):
    __slots__ = 'color'         # дублировать атрибуты width и height не надо, они возьмутся из родительского класса,
                                # достаточно просто расширить поведение

    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.color = c

d = Square(11, 7, 'red')
print(d.width, d.height, d.color)
print('--------------------------------------------------------------------')

#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------

# Если не хотим расширять поведение, но при этом запретить добавление атрибутов,
# то можно просто задать пустой __slots__
class Square(Rectangle):
    __slots__ = tuple()

    def __init__(self, a, b):
        super().__init__(a, b)

t = Square(34, 2)
print(t.width, t.height)
print('--------------------------------------------------------------------')

#-------------------------------------------------------------------------------
