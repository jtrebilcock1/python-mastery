'''works for getting the number of shares and cost as long as they are in the same order
which they are in this file. could also do unit tests'''
def read_file(infile):
	totalcost = 0
	with open('data/portfolio1.dat', 'r') as myfile:
		
		linelist = [line.split() for line in myfile]

		for line in linelist:	
			cost = int(line[1]) * float(line[2])
			totalcost += cost
		
		return totalcost

if __name__ == '__main__':
	filepath = 'data/portfolio1.dat'
	print(read_file(filepath))

	