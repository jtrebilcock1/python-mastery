class Stock:
	__slots__ = ['name','shares','price']
	amount_joe_knows_about = 0
	def __init__(self, name, shares, price):
		self.name = name
		self.shares = shares
		self.price = price
	def cost(self):
		return self.shares * self.price
	
	
	
s = Stock('GOOG',100,490.10)
print('%10s %10d %10.2f' % (s.name, s.shares, s.price))