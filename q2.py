import math
import random
numBoats = 0
numRaces = 0

def calculateScore(position):
	return int(101 + 1000*math.log(numBoats) - 1000*math.log(position))

def runRace(results):
	used = []

	for key in results:
		rndNum = random.randrange(1, (numBoats + 1), 1)
		while rndNum in used:
			rndNum = random.randrange(1, (numBoats + 1), 1)

		results[key].append(rndNum)
		used.append(rndNum)
	return results
 
def runRaceOlympic(results):
	used = []

	for key in results:
		rndNum = random.randrange(1, (numBoats + 1), 1)
		while rndNum in used:
			rndNum = random.randrange(1, (numBoats + 1), 1)

		results[key].append(calculateScore(rndNum))
		used.append(rndNum)
	return results

def totalScore(boat):
	scores = boat[1]
	scores = sorted(scores, reverse = True)

	return (sum(scores) - scores[0])

def totalScoreOlympic(boat):
	scores = boat[1]
	scores = sorted(scores)

	return (sum(scores) - scores[0])
 
def displayFigure(finalscores, finalscoresOlympic):
    import matplotlib.pyplot as plt
    
    plt.figure(1)
    plt.subplot(211)
    plt.hist(finalscores)
    plt.title("Score Distribution")
    
    plt.subplot(212)
    plt.hist(finalscoresOlympic)
    
    plt.savefig("figure.png")


def main():
	finalscores = {n: [] for n in range(numBoats)}
	finalscoresOlympic = {n: [] for n in range(numBoats)}

	for x in range(0, numRaces):
		finalscores = runRace(finalscores)
		finalscoresOlympic = runRaceOlympic(finalscoresOlympic)

	for key in finalscoresOlympic:
		finalscoresOlympic[key] = totalScoreOlympic((key, finalscoresOlympic[key]))

	for key in finalscores:
		finalscores[key] = totalScore((key, finalscores[key]))

	scoreslist = list(finalscores.values())
	scoreslistOlympic = list(finalscoresOlympic.values())
	displayFigure(scoreslist, scoreslistOlympic)
      
numBoats = int(input("Enter number of boats: "))
numRaces = int(input("Enter number of races: "))
main()