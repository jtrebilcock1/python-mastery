import csv
from sys import intern

def read_csv_as_dicts(in_csv, coltypes):
	
	with open(in_csv) as f:
		rows = csv.reader(f)
		headers = next(rows)	
		out = []
	
		for row in rows:
			out.append({ name:func(val) for name, func, val in zip(headers, coltypes, row) })
		
	return out

def read_csv_as_instances(filename, cls):
	'''
	Read a CSV file into a list of instances
	'''
	records = []
	with open(filename) as f:
		rows = csv.reader(f)
		headers = next(rows)
		for row in rows:
			records.append(cls.from_row(row))
	return records
