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

#read_csv_as_dicts('Data/ctabuss.csv', [intern, intern, int, float])