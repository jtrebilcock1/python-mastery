import csv

class Stock:
	@staticmethod
	def aTestClassMethod():
		print(f'aaaaaaaa')
		
	debug=False
	__slots__ = ['name','shares','price']
	amount_joe_knows_about = 0
	def __init__(self, name, shares, price):
		self.name = name
		self.shares = shares
		self.price = price
		
	def cost(self):
		return round(int(self.shares) * float(self.price),2)
	
	def sell(self, amount):
		self.shares-= amount
		
def print_portfolio(portfolio):
	for p in portfolio:
		print(f"{p.name:<25}{p.shares:<25}{p.price:<25}")
		
	
def read_portfolio(in_csv):
	with open(in_csv) as f: 
		rows = csv.reader(f)
		headings = next(rows)     # Skip headers	
		return [Stock(*row) for row in rows]
			

#stuff = read_portfolio('Data/portfolio.csv')
#print_portfolio(stuff)