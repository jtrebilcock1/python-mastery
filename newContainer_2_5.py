# readrides.py

import collections
...
class RideData(collections.Sequence):
	def __init__(self):
		self.routes = []      # Columns
		self.dates = []
		self.daytypes = []
		self.numrides = []
		
	def __len__(self):
		# All lists assumed to have the same length
		return len(self.routes)

	def __getitem__(self, index):
		return { 'route': self.routes[index],
		         'date': self.dates[index],
		         'daytype': self.daytypes[index],
		         'rides': self.numrides[index] }

	def append(self, d):
		self.routes.append(d['route'])
		self.dates.append(d['date'])
		self.daytypes.append(d['daytype'])
		self.numrides.append(d['rides'])		
a = RideData()