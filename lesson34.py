# Исключения (exceptions)

# Виды:
# 1) исключения выполнения
# 2) исключения компиляции

# Все исключения это классы
# Все они происходят от класса BaseException

print('hello')
print('hello2')

try:
 print('hello3')        # исключение компиляции
except:
    pass

try:
    'hello'[9]          # исключение выполнения
except:
    print()

try:
    a+b                 # исключение выполнения
except:
    print()

try:
    int('hello')
except ValueError:      # except выполняется только при возникновении исключения
    print('неправильное преобразование')

print('hello4')
print('hello5')
print('hello6')
print('-------------------------------------------------------')

# Все исключения это классы, значит мы можем создать экземпляр этого класса
t = IndexError()
print(t)
print(isinstance(t, IndexError))
print(isinstance(t, LookupError))
print(isinstance(t, TypeError))
print(isinstance(t, Exception))
print('-------------------------------------------------------')

try:
    [1, 2][5]
except IndexError:
    print('неправильный индекс')

try:
    [1, 2][8]
except LookupError:                 # можно обращаться не конкретно к IndexError, а к его родителю
    print('неправильный индекс')    # но при этом будут также отлавливаться все исключения наследующие данного родителя

try:
    {}[4]                           # по факту будет вызвано исключение KeyError
except LookupError:                 # но здесь оно будет отловлено, так как является потомком LookupError
    print('неправильный индекс')

print('-------------------------------------------------------')

# Исключения можно вызывать самомостоятельно
#raise ValueError('Неправильное значение')

# или
try:
    try:
        a = int(input())
    except:
        raise ValueError('Неправильное значение, передайте число')
except ValueError as ve:
    print(ve)
