class Basket:
	name = 'Basket'
	size = 10

	def putin(self, obj):
		if obj.size <= self.size:
			print(obj.name, 'in {}!'.format(self.name))
			self.size -= obj.size
		else:
			print('You cant put {} in!'.format(obj.name))

class Pack(Basket):
	name = 'Pack'
	size = 5


class Object:
	def __init__(self, name, size):
		self.size = size
		self.name = name

obj = Object('milk', 3)
obj1 = Object('beer', 2)
obj2 = Object('paper', 5)

basket = Basket()
pack = Pack()

basket.putin(obj)
basket.putin(obj1)
basket.putin(obj2)
basket.putin(obj2)
pack.putin(obj)
pack.putin(obj1)
pack.putin(obj2)
