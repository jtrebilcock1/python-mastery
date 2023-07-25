import csv

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

def read_rides_as_tuples(filename):
	'''
	Read the bus ride data as a list of tuples
	'''
	records = []
	with open(filename) as f:
		rows = csv.reader(f)
		headings = next(rows)     # Skip headers
		for row in rows:
			route = row[0]
			date = row[1]
			daytype = row[2]
			rides = int(row[3])
			record = (route, date, daytype, rides)
			records.append(record)
	return records

def read_rides_as_dicts(filename):
	'''
	Read the bus ride data as a list of dicts
	'''
	records = []
	with open(filename) as f:
		rows = csv.reader(f)
		headings = next(rows)     # Skip headers
		for row in rows:
			route = row[0]
			date = row[1]
			daytype = row[2]
			rides = int(row[3])
			record = {
			    'route': route, 
			    'date': date, 
			    'daytype': daytype, 
			    'rides' : rides
			}
			records.append(record)
	return records

class Row:
	# slots may limit peak memory usage
	__slots__ = ('route', 'date', 'daytype', 'rides')
	def __init__(self, route, date, daytype, rides):
		self.route = route
		self.date = date
		self.daytype = daytype
		self.rides = rides

# Uncomment to use a namedtuple instead
#from collections import namedtuple
#Row = namedtuple('Row',('route','date','daytype','rides'))

def read_rides_as_instances(filename):
	'''
	Read the bus ride data as a list of instances
	'''
	records = []
	with open(filename) as f:
		rows = csv.reader(f)
		headings = next(rows)     # Skip headers
		for row in rows:
			route = row[0]
			date = row[1]
			daytype = row[2]
			rides = int(row[3])
			record = Row(route, date, daytype, rides)
			records.append(record)
	return records

def read_rides_as_columns(filename):
	#works the same as the RideData class
	routes = []
	dates = []
	daytypes = []
	numrides = []
	with open(filename) as f:
		rows = csv.reader(f)
		headings = next(rows)     # Skip headers
		for row in rows:
			routes.append(row[0])
			dates.append(row[1])
			daytypes.append(row[2])
			numrides.append(int(row[3]))
	return dict(routes=routes, dates=dates, daytypes=daytypes, numrides=numrides)

if __name__ == '__main__':
	import tracemalloc
	tracemalloc.start()
	funk = [read_rides_as_tuples, read_rides_as_dicts,read_rides_as_instances]
	for f in funk:
		print(str(f))
		read_rides = f # Change to as_dicts, as_instances, etc.
		rides = read_rides("Data/ctabus.csv")
		print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())