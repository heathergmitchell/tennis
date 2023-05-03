import random
import numpy

def deuce():
	global scoreA
	global scoreB
	result = 0
	deuceA == 3
	deuceB == 3
	deuce = True
	advA = False #Player A wins adv point-> 40-40 or Game
	advB = False #Player B wins ad point-> 40-40 or Game
	while(scoreA < 4 and scoreB < 4):
		deuce = True
		print("Deuce")
		while(deuce == True):
			point = random.randint(0,100)
			if(point <= 50):
				advA = True
				deuce = False
				print("Advantage Player A")
			else:
				advB = True
				deuce = False
				print("Advantage Player B")
		point = random.randint(0,100)
		if(advA == True and point <= 50):
			scoreA += 1
			print("Player A wins!")
		elif(advA == True and point > 50):
			advA = False
			deuce = True
			print("Back to Deuce!")

		elif(advB == True and point <= 50):
			advB = False
			deuce = True
			print("Back to Deuce")
		else:
			scoreB += 1
			print("Player B wins!")

if __name__ == '__main__':
	print("Welcome to your tennis match! We'll get started with the coin toss to see which player goes first")
	coinToss = input('Enter 0 for Heads or 1 for Tails: ')

	x = random.randint(0,1)
	print("Coin toss was: ", x)

	lineup = []

	if(int(coinToss) == x):
		print(x)
		print("Congratulations! You won the coin toss and get to play first")
		lineup.append("You")
		lineup.append("Opponent")
		counter = 0
	else:
		print(x)
		print("Sorry! You lost the coin toss and your opponent will serve first")
		lineup.append("Opponent")
		lineup.append("You")
		counter = 1

	point = random.randint(0,100)

	scoreA = 0
	scoreB = 0

	deuceA = 0
	deuceB = 0

	score = ['Love', '15', '30', '40', '60', 'too far']
	sequence = max(scoreA,scoreB)
	fortyall = ['Deuce', 'Ad-In', 'Ad-Out']



	while (sequence < 4):
		print(point)

		if( scoreA ==3 and scoreB ==3):
			deuce()
		elif(point <= 50):
			print("Player A wins the point")
			scoreA += 1
		else:
			print("Player B gets the point")
			scoreB += 1
		print(lineup[0] + " vs. " + lineup[1])
		print(score[scoreA] + "-" + score[scoreB])
		point = random.randint(0,100)


		sequence = max(scoreA, scoreB)
	print(sequence)

	if (sequence == 4):
		print("The match is over")
	if (scoreA ==4):
		print("Player A wins")
	elif (scoreB == 4):
		print("Player B wins")
