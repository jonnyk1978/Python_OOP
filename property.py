# Практикуемся с property

from string import digits

class User:
	def __init__(self, login, password):
		self.login = login
		self.password = password


# Проблема
q = User('Ivan', 123)
print(q.password)					# Можно напрямую обращаться к аттрибутам класса
q.password = 321					# А также изменять их
print(q.password)
print('-----------------------------------------------------------------')
###############################################################################

# Требуется ограничить тип и качество вводимых данных, а также доступ к определённым аттрибутам
# Для этого и используется property

class User:
	def __init__(self, login, password):
		self.login = login
		self.__password = password

	# Используем для этого декоратор
	# По умолчанию это будет get-тер
	@property
	def password(self):
		print('getter called')
		return self.__password

	@staticmethod		# Вешаем декоратор staticmethod, чтобы не было неявной передачи экземпляра класса
	def is_include_number(password):
		for digit in digits:
			if digit in password:
				return True
		return False

	# Добавляем set-тер
	@password.setter
	def password(self, value):
		print('setter called')

		# Добавляем ограничение на качество вводимых данных
		if not isinstance(value, str):
			raise TypeError('Password must be a string')
		if len(value) < 4:
			raise ValueError('Password must be at least 4 characters')
		if not User.is_include_number(value):
			raise ValueError('Password must contain at least 1 digit')

		self.__password = value


a = User('aaa', 'AUIYFak')
print(a.password)						# getter called
a.password = 'akuyfsuipask'				# setter called, вызовет исключение ValueError

print('-----------------------------------------------------------------')
###############################################################################

# При создании экземпляра тоже хотелось бы проводить все проверки, что и в set-тере

class User:
	def __init__(self, login, password):
		self.login = login
		self.password = password		# обращение к имени свойства (self.password) вызовет set-тер

	# Используем для этого декоратор
	# По умолчанию это будет get-тер
	@property
	def password(self):
		print('getter called')
		return self.__password

	@staticmethod		# Вешаем декоратор staticmethod, чтобы не было неявной передачи экземпляра класса
	def is_include_number(password):
		for digit in digits:
			if digit in password:
				return True
		return False

	# Добавляем set-тер
	@password.setter
	def password(self, value):
		print('setter called')

		# Добавляем ограничение на качество вводимых данных
		if not isinstance(value, str):
			raise TypeError('Password must be a string')
		if len(value) < 4:
			raise ValueError('Password must be at least 4 characters')
		if not User.is_include_number(value):
			raise ValueError('Password must contain at least 1 digit')

		self.__password = value

b = User('bbbnn', 'AUIYFak')			# вызовет исключение, потому что пароль не содержит цифр

