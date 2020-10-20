# Обработка исключений

try:
	int('567')
#	int('hello')				# получение исключения сразу же переводит вполнение программы на блок except
#	1/0
	a+b
except ValueError:
	print('error ValueError')
except ZeroDivisionError:
	print('error ZeroDivisionError')
except NameError:
	print('error NameError')

###############################################################################

s = 'hello'
try:
	s[6]
except IndexError:
	print('error IndexError')

###############################################################################

s = 'hello'
d = {}
try:
	s[6]
except LookupError:					# выше по иерархии чем IndexError
	print('error LookupError --> IndexError')
try:
	d['key']
except LookupError:
	print('error LookupError --> KeyError')
print()

###############################################################################

try:
	4 + 'wtr'
except:							# аналог BaseException
	print('error')
finally:						# отработает независимо от появления исключения
	print('end')
print()

###############################################################################

try:
	1/0
except (KeyError, IndexError):		# указать несколько исключений
	print('Lookup Error')
except ZeroDivisionError:
	print('ZeroDivision error')
else:								# если исключения не случилось
	print('good')
finally:
	print('end')
