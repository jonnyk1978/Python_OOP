# инструкция raise

try:
	print(1/0)
except (KeyError, IndexError) as error:
	print('LookupError')
	print()
	print(f"Logging error: {error} {repr(error)}")
except ZeroDivisionError as zde:
	print("ZeroDivisionError")
	print()
	print(str(zde), "   ", repr(zde))

print('-------------------------------------------------------------------')

try:
	{}['k']
except (KeyError, IndexError) as error:
	print('LookupError')
	print()
	print(f"Logging error: {error} {repr(error)}")
except ZeroDivisionError as zde:
	print("ZeroDivisionError")
	print()
	print(str(zde), "   ", repr(zde))

print('-------------------------------------------------------------------')

try:
	[1, 2, 3][15]
except (KeyError, IndexError) as error:
	print('LookupError')
	print()
	print(f"Logging error: {error} {repr(error)}")
except ZeroDivisionError as zde:
	print("ZeroDivisionError")
	print()
	print(str(zde), "   ", repr(zde))

print('-------------------------------------------------------------------')

# генерация исключения
# raise KeyError					# явный вызов исключения
a = TypeError()						# создание экземпляра исключения
# raise a							# вызов исключения через экземпляр, который должен наследоваться от BaseException

a = TypeError("Ошибка типа")		# Указание текста ошибки, при создании экземпляра исключения
print(str(a))
print(a.args)
b = TypeError(1, 2, 3, 4, 5)
print(b.args)

print('-------------------------------------------------------------------')

try:
	[1, 2, 3][15]
except (KeyError, IndexError) as error:
	print(f"*** Logging error: {error} ***")	# Логгируем ошибку в консоль и пробрасываем исключение дальше
#	raise error
#	raise										# экземпляр исключения можно не указывать, он известен при входе в блок except

print('-------------------------------------------------------------------')

try:
	[1, 2, 3][15]
except (KeyError, IndexError) as error:
	print(f"*** Logging error: {error} ***")	# Логгируем ошибку в консоль и пробрасываем исключение дальше
	# Можно сгененировать/пробросить исключение другого типа, отличного от случившегося
	# Однако интерпретатор выдаст предупреждение:
	# During handling of the above exception, another exception occurred:
#	raise TypeError('Ошибка типа')

print('-------------------------------------------------------------------')

try:
	[1, 2, 3][15]
except (KeyError, IndexError) as error:
	print(f"*** Logging error: {error} ***")	# Логгируем ошибку в консоль и пробрасываем исключение дальше
	# Можно сгененировать/пробросить исключение другого типа, отличного от случившегося
	# Однако интерпретатор выдаст предупреждение:
	# During handling of the above exception, another exception occurred:
	# Если указать from None, то в консоль выведется только то исключение, которые мы выбросили
#	raise TypeError('Ошибка типа') from None

print('-------------------------------------------------------------------')

try:
	[1, 2, 3][15]
except (KeyError, IndexError) as error:
	print(f"*** Logging error: {error} ***")	# Логгируем ошибку в консоль и пробрасываем исключение дальше
	# During handling of the above exception, another exception occurred:
	# Если указать from error, то в консоль выведется вся иерархия полученных исключений,
	# c указанием того, что данное исключение было выброшено напрямую в пределах данной иерархии
	# The above exception was the direct cause of the following exception:
#	raise TypeError('Ошибка типа') from error

print('-------------------------------------------------------------------')

# ValueError -> TypeError -> Exception
try:
	raise ValueError('Ошибка значения')
except ValueError as ve:
	try:
		raise TypeError('Ошибка типа')
	except TypeError as te:
		# from ve скроет сообщение об исключении TypeError
		raise Exception('Большое исключение') from ve
