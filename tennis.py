import random
import numpy

if __name__ == '__main__':
	print("Welcome to your tennis match! We'll get started with the coin toss to see which player goes first")
	coinToss = input('Enter 0 for Heads or 1 for Tails: ')

	x = random.randint(0,1)

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

	#Probability of Player A winning a rally
	#Player A is whoever won the coin toss
	probA = 0.5

	#Probability of Player B winning a rally
	probB = 0.5

	scoreA = 0

	scoreB = 0

	score = ['Love', '15', '30', '40']

	while (scoreA != 4 or scoreB != 4 or (scoreA == 3 and scoreB == 3)):
		rand = random.random()

		if(counter % 2 == 0):	#Player A is serving
			if(rand < probA or rand == probA):	#Player A won point
				scoreA += 1
			else:		#Player A lost point
				scoreB += 1
		else:	#Player B is serving
			if(rand < probB or rand == probB):	#Player B won point
				scoreB += 1
			else:	#Player B lost point
				scoreA += 1

		print(lineup[0] + " vs. " + lineup[1])
		print(score[scoreA] + "-" + score[scoreB])

		if(scoreA == 4):
			print(lineup[0] + " won first game. Final score: ")
			print(score[scoreA] + "-" + score[scoreB])
			scoreA = 0
			scoreB = 0
			counter += 1
			break
		elif(scoreB == 4):
			print(lineup[1] +  " won first game. Final score: ")
			print(score[scoreA] + "-" + score[scoreB])
			scoreA = 0
			scoreB = 0
			counter += 1
			break
		elif (scoreA == 3 and scoreB == 3):
			print(lineup[0]+ " vs. "+ lineup[1])
			print("Deuce")
			break
		print(rand)

	fortyall = ['Deuce', 'Ad-In', 'Ad-Out']

	#Deuce
	if(scoreA == 3 and scoreB == 3):
		deuceScoreA = 0
		deuceScoreB = 0

		while(deuceScoreA != 2 or deuceScoreB != 2):
			if(counter % 2 == 0):	#Player A serving
				if(rand < probA or rand == probA):	#Player A won the point
					deuceScoreA +=1
					print(lineup[0] + " vs. " + lineup[1])
					print("Advantage In")
				else: #Player A lost point
					deuceScoreB += 1
					print(lineup[0] + " vs. " + lineup[1])
					print("Advantage Out")
					if(deuceScoreA != 0):
						deuceScoreA -=1
			else:	#Player B serving
				if(rand < probB or rand == probB):	#Player B won point
					deuceScoreB += 1
					print(lineup[0] + " vs. " + lineup[1])
					print("Advantage In")
				else:	#Player B lost point
					deuceScoreA +=1
					print(lineup[0] + " vs. " +  lineup[1])
					print("Advantage Out")
					if (deuceScoreB != 0):
						deuceScoreB -= 1

			if(deuceScoreA == 2):
				print(rand)
				print(lineup[0] + " won first game")
				print("Ad vs. " + score[scoreB])
				break
			elif(deuceScoreB == 2):
				print(rand)
				print(lineup[1] + " won first game")
				print(score[scoreA] + " vs. Ad")
				break
			print(rand)

