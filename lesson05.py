# Методы экземпляра

class Cat:
    breed = 'pers'

#    def hello():
    def hello(*args):
        print("Hello world from kitty", args)

    def show_breed(instance):
        print(f'my breed is {instance.breed}')

    def show_name(instance):
        if hasattr(instance, 'name'):               # Проверяем есть ли у экземпляра атрибут name
            print(f'my name is {instance.name}')
        else:
            print('Nothing')

    def set_value(koshka, value, age=0):
        koshka.name = value
        koshka.age = age

    def new_method(self):                           # В качестве имени аргумента метода, обозначающего экземпляр,
        pass                                        # от которого происходит вызов метода принято использовать self

bob = Cat()
#bob.hello()                # выдаст ошибку TypeError

print(Cat.hello)            # Это функция
print(bob.hello)            # Это метод (Функция, объявленная внутри класса. Метод привязан к конкретному объекту)
                            # При вызове метода, тот объект, с которым он связан, будет автоматически проставляться в аргумент функции класса
print()

jim = Cat()
jim.hello()                 # Видим адрес памяти в котором находится экземпляр jim
print(jim)                  # Видим адрес памяти в котором находится экземпляр jim, совпадает с предыдущим
print()

bob = Cat()                 # Пересоздадим экземпляр bob
bob.hello()                 # Видим адрес памяти в котором находится экземпляр bob
print(bob)                  # Видим адрес памяти в котором находится экземпляр bob, совпадает с предыдущим
print()

# bob и jim - это два разных экземпляра

a = [1, 2, 3]
b = [5, 3, 4]
b.sort()                    # Интерпретатор понимает какой экземпляр передать в качестве аргумента методу sort(), это экземпляр b
                            # Метод обязательно связывается с объектом, из которого он был вызван
print(b)
print()

walt = Cat()                # Создаём экземпляр walt
print(walt.__dict__)
walt.show_breed()           # И вызываем метод show_breed()
walt.breed = 'siam'         # Изменяем атрибут breed у экземпляра walt
print(walt.__dict__)        # При этом данный атрибут становится частью пространства имён экземпляра
print(walt.breed)
print()

bob = Cat()                 # Пересоздадим экземпляр bob
bob.show_breed()            # bob по-прежнему pers
print()

mary = Cat()                # Создадим экземпляр Cat по имени mary
#mary.show_name()           # Выдаст ошибку AttributeError, потому что атрибута name в классе Cat нет
mary.name = 'MARY'          # Добавляем атрибут в экземпляр mary
mary.show_name()            # И теперь вызов метода show_name из экземпляра mary не вызывает ошибку
print()

tom = Cat()
tom.show_name()             # Получаем Nothing, потому что атрибута name в классе Cat нет
tom.set_value('Tom')        # Вызываем метод set_value экземпляра tom класса Cat для установки атрибута name в объекте tom
tom.show_name()             # Получаем Tom, потому что атрибута name в классе Cat нет
#tom.set_value()            # Выдаст ошибку TypeError (не хватает аргумента)
print()

jerry = Cat()               # Создадим экземпляр Cat по имени jerry
jerry.set_value('Jerry')    # Второй аргумент примет значение по умолчанию
print(jerry.name + ' - ' + str(jerry.age))
jerry = Cat()               # Пересоздадим экземпляр Cat по имени jerry
jerry.set_value('Jerry', 15)# Второй аргумент укажем явно
print(jerry.name + ' - ' + str(jerry.age))
print()

jerry.new_method()
