# Методы сравнения экземпляров
# __eq__ - отвечае за ==
# __ne__ - отвечае за !=
# __lt__ - отвечае за <
# __le__ - отвечае за <=
# __gt__ - отвечае за >
# __ge__ - отвечае за >=

class Rectangle0:
    def __init__(self, a, b):
        self.a = a
        self.b = b

v = Rectangle0(1, 2)
r = Rectangle0(4, 5)
d = Rectangle0(1, 2)
try:
    print(v>r)              # Операция сравнения не поддерживается для данных сущностей
except TypeError as te:
    print(te)
try:
    print(v<=r)              # Операция сравнения не поддерживается для данных сущностей
except TypeError as te:
    print(te)
try:
    print(v==r)              # Ошибку не выдаст, но ответом всегда будет False, потому что сравнение идёт по id
except TypeError as te:
    print(te)
try:
    print(v==d)              # Ошибку не выдаст, но ответом всегда будет False, потому что сравнение идёт по id
except TypeError as te:
    print(te)
print('-----------------------------------------------------------------------')



# Добавим поведение классу
class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.a * self.b

    def __eq__(self, other):
        print('__eq__ called')
        if isinstance(other, Rectangle):
            if self.a == other.a and self.b == other.b:
                return True
            else:
                return False
        else:
            return False

    # Less Then (будем сравнивать например по площади)
    def __lt__(self, other):
        print('__lt__ called')
        if isinstance(other, Rectangle):
            if self.area < other.area:
                return True
            else:
                return False
        elif isinstance(other, (int, float)):
            if self.area < other:
                return True
            else:
                return False
        else:
            return False

    # Less or Equal (реализуем с помощью методов __eq__ и __lt__)
    def __le__(self, other):
        print('__le__ called')
        # self == other вызовет __eq__
        # self < other вызовет __lt__
        return self == other or self < other

a = Rectangle(7, 5)
b = Rectangle(5, 9)
c = Rectangle(7, 5)
print(f'a({a.a}, {a.b}) == b({b.a}, {b.b}) - {a == b}')     # Скрытый вызов __eq__
print(f'a({a.a}, {a.b}) == c({c.a}, {c.b}) - {a == c}')     # Скрытый вызов __eq__
print('-----------------------------------------------------------------------')
print(f'a({a.a}, {a.b}, S={a.area}) < b({b.a}, {b.b}, S={b.area}) - {a < b}')       # Скрытый вызов __lt__
print(f'a({a.a}, {a.b}, S={a.area}) < c({c.a}, {c.b}, S={c.area}) - {a < c}')       # Скрытый вызов __lt__
print(f'a({a.a}, {a.b}, S={a.area}) < {100}) - {a < 100}')                          # Скрытый вызов __lt__ (сравнение экземпляра с числом)
print('-----------------------------------------------------------------------')

# Выдаст ошибку TypeError при попытке вызвать операцию '<' с Rectangle (100 < b?, числа не поддерживают эту операцию),
# после чего интерпретатор попробует узнать, поддерживает ли Rectangle операцию '>' с числами,
# но поскольку метод __gt__ для Rectangle не определён, поэтому и выдаётся ошибка TypeError
# Добавим данное поведение в класс и ошибка уйдёт
try:
    print(f'{100} < b({b.a}, {b.b}, S={b.area}) - {100 < b}')
except TypeError as te:
    print(f'{100} < b({b.a}, {b.b}, S={b.area})')
    print(te)
print('-----------------------------------------------------------------------')
# И вообще интерпретатор при отсутствии метода __gt__ попытается поменять аргументы местами и вызвать метод __lt__
# (аналогично и с другими противоположными методами)
# Скрытый вызов __gt__ (операция >), но вызывается __lt__, поскольку __gt__ не определён
print(f'a({a.a}, {a.b}, S={a.area}) > b({b.a}, {b.b}, S={b.area}) - {a > b}')
print('-----------------------------------------------------------------------')

# <= меньше или равно
print(f'a({a.a}, {a.b}, S={a.area}) <= b({b.a}, {b.b}, S={b.area}) - {a <= b}') # неявный вызов метода __le__, который дёрнет __eq__ и/или __lt__
print(f'a({a.a}, {a.b}, S={a.area}) <= c({c.a}, {c.b}, S={c.area}) - {a <= c}') # неявный вызов метода __le__, который дёрнет __eq__ и/или __lt__
print('-----------------------------------------------------------------------')

# != не равно
# неявный вызов метода __ne__, который дёрнет и вернёт противоположный результат __eq__, поскольку __ne__ не определён
# т.е. интерпреатор a!=b переделаёт в not(a==b)
print(f'a({a.a}, {a.b}, S={a.area}) != b({b.a}, {b.b}, S={b.area}) - {a != b}')
print('-----------------------------------------------------------------------')
# по этой же причине мы можем использовать операцию >= хотя метод __ge__ не определён,
# поскольку в данном случае вызовется метод __le__
print(f'a({a.a}, {a.b}, S={a.area}) >= b({b.a}, {b.b}, S={b.area}) - {a >= b}')     # __ge__ -> __le__ -> __eq__ и __lt__
print('-----------------------------------------------------------------------')
print(f'a({a.a}, {a.b}, S={a.area}) >= c({c.a}, {c.b}, S={c.area}) - {a >= c}')     # __ge__ -> __le__ -> __eq__, __lt__ не вызвался потому что __eq__ вернул True
print('-----------------------------------------------------------------------')
