'''works for getting the number of shares and cost as long as they are in the same order
which they are in this file. could also do unit tests'''
def portfolio_cost(infile):
	totalcost = 0
	with open(infile, 'r') as myfile:
		
		linelist = [line.split() for line in myfile]

		for count, line in enumerate(linelist):	
			try:
				cost = int(line[1]) * float(line[2])
				totalcost += cost
			except ValueError as e:
				print(e)
				print(f'----cant parse line(#{count+1}) reading: {" ".join(line)}' )
				
		
		return totalcost

if __name__ == '__main__':
	filepath = 'data/portfolio2.dat'
	print(portfolio_cost(filepath))

