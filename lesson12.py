# Вычисляемые property

class Square:
    def __init__(self, s):
        self.side = s

    def area(self):
        return(self.side**2)

a = Square(5)
print(a.area())
print('------------------')



class Square2:
    def __init__(self, s):
        self.side = s

    # "превращаем" метод в свойство (декорируем)
    # минус - метод запускается/вычисляется КАЖДЫЙ раз при обращении к нему,
    # даже если атрибут side не изменяется
    @property
    def area(self):
        return(self.side**2)

b = Square2(6)
print(b.area)                   # обращаемся к методу, как к атрибуту
b.side = 10                     # меняем один атрибут
print(b.area)                   # обращаемся к методу, как к атрибуту, и получаем как будто бы изменённый атрибут
print('------------------')



class Square3:
    def __init__(self, s):
        self.side = s
        self.__area = None

    @property
    def area(self):

        if self.__area is None:
            print('Calculate area')
            self.__area = self.side ** 2

        return self.__area

c = Square3(11)
print(c.area)                   # обращаемся к методу, как к атрибуту, вычисление площади происходит только в 1-й раз
c.side = 22                     # меняем атрибут
print(c.area)                   # однако площадь по новой не вычисляется
print('------------------')



class Square4:
    def __init__(self, s):
        self.__side = s
        self.__area = None
        self.__perimeter = None

    @property           # геттер
    def side(self):
        return self.__side

    @side.setter        # сеттер
    def side(self, value):
        self.__side = value     # изменяем сторону
        self.__area = None      # значит площадь придётся вычислить заново
        self.__perimeter = None # значит пертиметр придётся вычислить заново

    @property
    def area(self):

        if self.__area is None:
            print('Calculate area')
            self.__area = self.side ** 2

        return self.__area

    # Домашнее задание
    @property
    def perimeter(self):

        if self.__perimeter is None:
            print('Calculate perimeter')
            self.__perimeter = self.side * 4

        return self.__perimeter

d = Square4(7)
print('P=' + str(d.perimeter) + ', S=' + str(d.area))   # обращаемся к методу, как к атрибуту, вычисление площади и периметра происходит только если сторона НЕ менялась
print('P=' + str(d.perimeter) + ', S=' + str(d.area))   # обращаемся к методу, как к атрибуту, вычисление площади и периметра происходит только если сторона НЕ менялась
print('P=' + str(d.perimeter) + ', S=' + str(d.area))   # обращаемся к методу, как к атрибуту, вычисление площади и периметра происходит только если сторона НЕ менялась
d.side = 22                     # меняем сторону
print('P=' + str(d.perimeter) + ', S=' + str(d.area))   # обращаемся к методу, как к атрибуту, вычисление площади и периметра происходит только если сторона НЕ менялась
print('------------------')
