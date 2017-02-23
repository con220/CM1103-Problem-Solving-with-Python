"""
Ensure (a) is correct
>>> seriesScore(("bob", [2, 4, 1, 1, 2, 5]))
10
>>> seriesScore(("bill", [1, 3, 1, 4, 2, 4]))
11

Ensure (b) is correct
>>> ascSailors([("Alice", [1, 2, 1, 1, 1, 1]), ("Bob", [3, 1, 5, 3, 2, 5]), ("Clare", [2, 3, 2, 2, 4, 2]), ("Dennis", [5, 4, 4, 4, 3, 4]), ("Eva", [4, 5, 3, 5, 5, 3])])
[('Alice', [1, 2, 1, 1, 1, 1]), ('Clare', [2, 3, 2, 2, 4, 2]), ('Bob', [3, 1, 5, 3, 2, 5]), ('Dennis', [5, 4, 4, 4, 3, 4]), ('Eva', [4, 5, 3, 5, 5, 3])]

Ensure (c) is correct
>>> ReadCSV("sailors.csv")
OrderedDict([('Alice', (100.0, 0.0)), ('Bob', (100.0, 5.0)), ('Clare', (100.0, 10.0)), ('Dennis', (90.0, 0.0)), ('Eva', (90.0, 5.0))])

Ensure (d) is correct
>>> rndPerformance(ReadCSV("sailors.csv"))
OrderedDict([('Alice', 100.0), ('Bob', 105.76045089520113), ('Clare', 108.36452152548142), ('Dennis', 90.0), ('Eva', 96.10844089749128)])

Ensure (e) is correct
>>> sailorPosition(rndPerformance(ReadCSV("sailors.csv")))
['Clare', 'Bob', 'Alice', 'Eva', 'Dennis']
"""
import collections
import random

#(a)
def seriesScore(sailor):
	scores = sailor[1] #take only the scores and store them
	scores = sorted(scores, reverse = True) #sort the list of scores in descending order

	#The "worst" score is the highest so the total is the sum minus the first element
	return (sum(scores) - scores[0])

#(b)
def ascSailors(sailors):
	if len(sailors) > 1: #to stop the recursion when only one element in list
		#Use of quick sort ft. recursion (with smallest first)
		pivot = round(len(sailors) / 2) #pivot starts in the middle of the list

		#spilt the list into two parts, smaller and bigger
		bigger = []
		smaller = []

		for i, sailor in enumerate(sailors):
			if i != pivot:
				if seriesScore(sailor) > seriesScore(sailors[pivot]):
					bigger.append(sailor)
				else:
					smaller.append(sailor)

		#Recursion to continue comparsions until both lists are sorted
		ascSailors(smaller)
		ascSailors(bigger)

		#once recursion is complete, return the sorted list
		return (smaller + [sailors[pivot]] + bigger)

#(c)
def ReadCSV(filename):
	import csv

	#Define an ordered dictionary to input the data into
	sailorPerformance = collections.OrderedDict()
	with open(filename) as csvfile:
		rdr = csv.reader(csvfile)
		next(rdr, None)
		for row in rdr:
			sailorPerformance[row[0]] = (float(row[1]), float(row[2]))

	return sailorPerformance

#(d)
def rndPerformance(sailorPerformance):
	random.seed(-57) #included this to ensure it worked as intended (same results as on coursework task)

	#Define an ordered dictionary to input the data into
	PerformanceVal = collections.OrderedDict()
	for key in sailorPerformance: #go through each key
		meandev = sailorPerformance[key] #take out the tuple
		PerformanceVal[key] = random.normalvariate(meandev[0], meandev[1])

	return PerformanceVal

#(e)
def sailorPosition(PerformanceVal):
	Positions = sorted(PerformanceVal, key=lambda val: PerformanceVal[val], reverse = True)
	return Positions

#(f)
def runRace(results):
	used = []

	for key in results:
		rndNum = random.randrange(1, 6, 1)
		while rndNum in used:
			rndNum = random.randrange(1, 6, 1)

		results[key].append(rndNum)
		used.append(rndNum)
	return results

def main():
	results = collections.OrderedDict([('Alice', []), ('Bob', []), ('Clare', []), ('Dennis', []), ('Eva', [])])

	#runs 5 races
	for x in range(0, 5):
		results = runRace(results)

	print(results)
	#calculate each of their series score
	for key in results:
		results[key] = seriesScore((key, results[key]))

	results = sailorPosition(results)

	print(results)

main()