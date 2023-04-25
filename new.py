import random

class Deuce:
	def deuce():
		deuceA = False #Player A wins deuce point-> Ad - 40
		deuceB = False #Player B wins deuce point-> 40 - Ad
		advA = False #Player A wins adv point-> 40-40 or Game
		advB = False #Player B wins ad point-> 40-40 or Game
		deuceEnd = False

		while(deuceEnd == False):
			if(point <= 50):
				advA = False
				advB = False
				deuceA = True
				point = random.randint(0, 100)

				if(point <= 50):
					advA = True
					scoreA += 1

				else:
					advB = True
					deuceA = False

			else:
				advA = False
				advB = False
				deuceB = True
				point = random.randint(0, 100)

				if(point <= 50):
					advA = True
					deuceB = False
				else:
					advB = True
					scoreB += 1

			point = random.randint(0, 100)

			if (deuceA == True and advA == True):
				deuceEnd = True
			elif(deuceB == True and advB == True):
				deuceEnd = True
