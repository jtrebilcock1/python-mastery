from readrides import read_rides_as_dicts
import collections


def number_routes(inlistdict):
	totals = collections.Counter()
	for k in inlistdict:
		totals[k['route']] +=1
	return len(totals)
	
def get_numberRiders_onADay(inlistdict, date, routename):
	d = collections.defaultdict(list)
	for row in inlistdict:
		if row['route'] == routename and row['date'] == date:
			d['rides'].append(row['rides'])
		
	return f'total passengers on {date} for bus route {routename} is {sum(d["rides"])}'	
	
def get_Rides_perRoute(inlistdict):
	totals = collections.Counter()
	for k in inlistdict:
		totals[k['route']] += k['rides']
	totals.most_common(3)
	return f'total number of passengers per route (top 3) are: {totals.most_common(3)}'
	
def best_10yr_route(inlistdict, start_yr):
	year1totals = collections.Counter()
	otherYearTotals = collections.Counter()
	for k in inlistdict:
		if k['date'].split('/')[2] == start_yr:
			year1totals[k['route']] += k['rides']
		
		
	for k in inlistdict:
		if k['date'].split('/')[2]:
			otherYearTotals[k['route']] += k['rides']		
	
	summary = {}
	for k in otherYearTotals:
		summary.update({k:(otherYearTotals[k] - year1totals[k])})
			
	return f'the top 5 most increased routes since 2001 are: {collections.Counter(summary).most_common(5)}'
		
def main():
	#load data as dict from csv
	ride_data = read_rides_as_dicts('Data/ctabus.csv')
	
	#get total number routes
	route_totals = number_routes(ride_data)
	print(f'the total number of bus routes is: {route_totals}')
	
	#get passenger count on a given day
	print(get_numberRiders_onADay(ride_data, '02/02/2011', '22'))
	
	#total passengers per route (top 3)
	print(get_Rides_perRoute(ride_data))
	
	#top 5 greatest change from 2001 to 2011 (tbh im going to whatever the most recent year is in the csv)
	#so it is really the top 5 where the total of year 1 is subtracted from the total of all year per route
	#instructions unclear if that is whats needed. if 2011 isnt latest in data just add a argument for end yr
	print(best_10yr_route(ride_data, '2001'))

if __name__ == '__main__':
	main()
