class A:
	
	__count = 0
	whatever = 'whatever'
	
	def get_count(self):
		return self.__count
	def set_count(self,count):
		self.__count = count
		
a=A()
print(a.get_count())

a.__count = 42
print(a.get_count())


print(a.__count)

a.set_count(100)


print(a.__count)