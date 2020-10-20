# Распространение исключений

def third():
	print('start third')
	try:
		1/0
	except ZeroDivisionError:
		print('--- handling ---')
	print('finish third')

def second():
	print('start second')
	third()
	print('finish second')

def first():
	print('start first')
	second()
	print('finish first')

print('hello')

first()

print()
print()
print()
###############################################################################

def third():
	print('start third')
	1/0
	print('finish third')

def second():
	print('start second')
	third()
	print('finish second')

def first():
	print('start first')
	try:
		second()
	except ZeroDivisionError:
		print('--- handling in first! ---')
	print('finish first')

print('hello')

first()
