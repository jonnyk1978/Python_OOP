# Магические методы
# Метод __call__

class Counter0:
    def __init__(self):
        print('init ojbect ', self)

# call (вызов) - это оператор вызова '()'
a = Counter0()       # сам класс является вызываемым, результатом вызова будет экземпляр класса
print(a)
print()
b = Counter0()       # сам класс является вызываемым, результатом вызова будет экземпляр класса
print(b)
print('---------------------------------------------------------')

try:
    a()                 # Экземпляр не является вызываемым, вызовет TypeError, но можно добавить такое поведение
except TypeError as te:
    print(te)
print('---------------------------------------------------------')



class Counter:
    def __init__(self):
        self.counter = 0
        self.summa = 0
        self.length = 0
        print('init ojbect ', self)

    def __call__(self, *args, **kwargs):
        self.counter+=1
        self.summa += sum(args)
        self.length += len(args)
        print(f'Object {self} called {self.counter} times')

    def average(self):
        return self.summa / self.length

b = Counter()
print(b)
print(b())              # Экземпляр класса стал вызываемым при помощи метода __call__
print('---')
print(b())              # Экземпляр класса стал вызываемым при помощи метода __call__
print('---')
print(b())              # Экземпляр класса стал вызываемым при помощи метода __call__
print('---')
print(b())              # Экземпляр класса стал вызываемым при помощи метода __call__
print('---')
print(b())              # Экземпляр класса стал вызываемым при помощи метода __call__
print('---')
print(b())              # Экземпляр класса стал вызываемым при помощи метода __call__
print('---')
print(b.counter)
print('---')

q = Counter()
print(f'Object: {q}')
print(f'Counter: {q.counter}')
print(f'Summa: {q.summa}')
print('---')
q(3, 4, 5)
print(f'Summa: {q.summa}')
print(f'Length: {q.length}')
print('---')
q(1, 2)
print(f'Summa: {q.summa}')
print(f'Length: {q.length}')
print('---')

r = Counter()
r(3, 4, 5, 6, 7)
print(r.average())
print('---')



from time import perf_counter

# Задекорируем наш метод __call__
class Timer:
    def __init__(self, func):
        self.fn = func

    def __call__(self, *args, **kwargs):
        print(f'Function {self.fn.__name__}')
        start = perf_counter()
        result = self.fn(*args, **kwargs)
        finish = perf_counter()
        print(f'The function {self.fn.__name__} worked in {finish - start}')
        return result


@Timer
def fact(n):
    pr = 1
    for i in range(1, n + 1):
        pr *= i
    return pr


def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)

fact = Timer(fact)

print(fact)         # Получаем экезмпляр класса Timer
fact(7)             #
