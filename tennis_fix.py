import random
import numpy

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

	score = ['Love', '15', '30', '40', '60']
	sequence = max(scoreA,scoreB)

	while (sequence < 4):
		print(point)

		if(point <= 50):
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
