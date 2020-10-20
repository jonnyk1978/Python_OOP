# Пользовательские исключения

# Все свои исключения рекомендуется наследовать от Exception,
# а не от BaseException

class MyException(Exception):
	def __str__(self):
		return("This is my first exception")

try:
	raise MyException						# выкидываем собственное исключение
except MyException as me:
	print(me)

###########################################################

class MyException(Exception):

	def __init__(self, *args):
		if args:
			self.message = args[0]
		else:
			self.message = None

	def __str__(self):
		print('str called')
		if self.message:
			return f"MyException ({self.message})"
		else:
			return "MyException is empty"

#raise MyException('hello', 1, 2, 3)
#raise MyException()

###########################################################
# Трёхуровневая иерархия исключений

class SnakeExceptionBase(Exception):
	"""Основной класс ошибок змейки"""

class SnakeBorderException(SnakeExceptionBase):
	"""Ошибка соприкосновения змеи со стенкой"""

class SnakeTailException(SnakeBorderException):
	"""Ошибка соприкосновения змеи с хвостом"""

