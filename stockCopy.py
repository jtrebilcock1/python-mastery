import csv
import validate
class Stock:
	
	debug=False
	__slots__ = ['name','_shares','_price']
	amount_joe_knows_about = 0
	_types = (str, int, float)
	
	def __init__(self, name, shares, price):
		self.name = name
		self.shares = shares
		self.price = price	
		
	def __repr__(self): #this lets us print instances in a readable way
		# Note: The !r format code produces the repr() string
		return f'{type(self).__name__}({self.name!r}, {self.shares!r}, {self.price!r})'	
	
	@staticmethod
	def aTestClassMethod():
		print(f'aaaaaaaa')
	
	@classmethod
	def from_row(cls, row):
		values = [func(val) for func, val in zip(cls._types, row)]
		return cls(*values)		
	
	@property
	def price(self):
		return self._price		
	@price.setter
	def price(self, value):
		#if not isinstance(value, self._types[2]):
			#raise TypeError('expected int')	
		validate.Float()
		if value <= 0:
			raise ValueError('price must be greater than 0')	
		self._price = value
		
	@property
	def shares(self):
		return self._shares		
	@shares.setter
	def shares(self, value):
		if not isinstance(value, self._types[1]):
			raise TypeError('expected int')
		if value < 0:
			raise ValueError('shares must be greater than or equal to 0')	
		self._shares = value
	
	@property
	def cost(self):
		return round(int(self.shares) * float(self.price),2)
	
	def sell(self, amount):
		self.shares-= amount
		
	def __eq__(self, other):
		#checks if it is also a member of stock then checks individual attributes
		return isinstance(other, Stock) and ((self.name, self.shares, self.price) == 
		                                     (other.name, other.shares, other.price))	
	
def print_portfolio(portfolio):
	for p in portfolio:
		print(f"{p.name:<25}{p.shares:<25}{p.price:<25}")
		
	
#def read_portfolio(in_csv):
	#with open(in_csv) as f: 
		#rows = csv.reader(f)
		#headings = next(rows)     # Skip headers	
		#return [Stock.from_row(row) for row in rows]
