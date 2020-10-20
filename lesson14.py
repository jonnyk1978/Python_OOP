# Пространство имён класса

# Методам будут видны именно эти, глобальные переменные, а не переменные класса
#PYTHON_DEV = 1
#GO_DEV = 1
#REACT_DEV = 1

class DeparmentIT:
    PYTHON_DEV = 4
    GO_DEV = 3
    REACT_DEV = 2

    def info0(self):
        print(PYTHON_DEV, GO_DEV, REACT_DEV)

    # Правильное обращение к атрибутам (вариант 1)
    # через атрибуты объекта
    def info1(self):
        print(self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV)

    # Правильное обращение к атрибутам (вариант 2)
    # через атрибуты класса
    def info2(self):
        print(DeparmentIT.PYTHON_DEV, DeparmentIT.GO_DEV, DeparmentIT.REACT_DEV)    # Правильное обращение к атрибутам

    # Правильное обращение к атрибутам (вариант 3)
    @property
    # через свойство (по сути тот же вариант 1)
    def info3(self):
        print(self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV)

    # Правильное обращение к атрибутам (вариант 4)
    # через метод класса (по сути тот же вариант 2)
    @classmethod
    def info4(cls):
        print(f'classmethod - {cls.PYTHON_DEV}, {cls.GO_DEV}, {cls.REACT_DEV}')

    # Правильное обращение к атрибутам (вариант 5)
    # через метод класса (по сути тот же вариант 2)
    @staticmethod
    def info5():
        print(f'staticmethod - {DeparmentIT.PYTHON_DEV}, {DeparmentIT.GO_DEV}, {DeparmentIT.REACT_DEV}')

    def make_backend(self):
        print('Python and Go')

    def make_frontend(self):
        print('React')

    def hiring_pyt_dev0(self):
        self.PYTHON_DEV = self.PYTHON_DEV + 1

    def hiring_pyt_dev(self):
        DeparmentIT.PYTHON_DEV = DeparmentIT.PYTHON_DEV + 1

it1 = DeparmentIT()
try:
    it1.info0()                     # Выдаст ошибку NameError, потому что методам недоступны переменные из класса
                                    # Будут взяты глобальные переменные
except NameError as ne:
    print(ne)

it1.info1()
it1.info2()
it1.info3
it1.info4()
it1.info5()
print('----------------------------------------------------')
it1.hiring_pyt_dev0()
print(it1.PYTHON_DEV)               # атрибут изменится только у экземпляра
print(DeparmentIT.PYTHON_DEV)       # а у класса останется прежним
print('----------------------------------------------------')
it1.hiring_pyt_dev()
print(it1.PYTHON_DEV)               # атрибут изменится у класса
print(DeparmentIT.PYTHON_DEV)
it2 = DeparmentIT()                 # а так же у всех, вновь создаваемых экземпляров
print(it2.PYTHON_DEV)
print('----------------------------------------------------')

