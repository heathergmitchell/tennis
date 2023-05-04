import random
import numpy

yourProb = 0
oppProb = 0

scoreYou = 0
scoreOpp = 0

gameScoreYou = 0
gameScoreOpp = 0

setScoreYou = 0
setScoreOpp = 0

youStart = False

counter = 0

def youServe():
	point = random.randint(0, 100)
	global yourProb

	global scoreYou
	global scoreOpp

	print(point)

	if(point <= yourProb):
		scoreYou += 1
	else:
		scoreOpp += 1

def oppServe():
	point = random.randint(0, 100)
	global oppProb

	global scoreYou
	global scoreOpp

	print(point)

	if(point <= oppProb):
		scoreOpp += 1
	else:
		scoreYou += 1

def game():
	global scoreYou
	global scoreOpp

	global gameScoreYou
	global gameScoreOpp

	global counter
	global youStart

	score = ['Love', '15', '30', '40', '40.']

	endGame = False

	while(endGame == False):
		if(scoreYou == 3 and scoreOpp == 3):
			deuce()
		else:
			if(youStart == True and counter % 2 == 0):
				youServe()
			elif(youStart == True and counter % 2 != 0):
				oppServe()
			elif(youStart != True and counter % 2 == 0):
				oppServe()
			elif(youStart != True and counter % 2 != 0):
				youServe()
			print("You vs. Opponent")
			print(score[scoreYou] + " - " + score[scoreOpp])

		if(scoreYou == 4):
			gameScoreYou += 1
			print("You won!")
			endGame = True
		elif(scoreOpp == 4):
			gameScoreOpp += 1
			print("Opponent won")
			endGame = True

	endGame = False
	scoreYou = 0
	scoreOpp = 0
	counter += 1

	print("Game score: You vs. Opponent")
	print(str(gameScoreYou) + " - " + str(gameScoreOpp))

def set():
	global gameScoreYou
	global gameScoreOpp
	global setScoreYou
	global setScoreOpp

	endSet = False

	while(endSet == False):
		if(gameScoreYou == 6 and gameScoreOpp == 6):
			print("tiebreaker")
			break
		else:
			game()

		if((((gameScoreYou == 6) and (gameScoreYou - gameScoreOpp >= 2)) or (gameScoreYou == 7 and gameScoreOpp == 5) or (gameScoreYou == 7 and gameScoreOpp == 6))):
			print("You vs. Opponent")
			print(str(gameScoreYou) + " - " + str(gameScoreOpp))
			setScoreYou += 1
			endSet = True
		elif(((gameScoreOpp == 6) and (gameScoreOpp - gameScoreYou >= 2)) or (gameScoreOpp == 7 and gameScoreYou == 5) or (gameScoreOpp == 6 and gameScoreYou == 5)):
			print("You vs. Opponent")
			print(str(gameScoreYou) + " - " + str(gameScoreOpp))
			endSet = True

	endSet = False
	gameScoreYou = 0
	gameScoreOpp = 0

def deuce():
	global scoreYou
	global scoreOpp
	global yourProb
	global oppProb
	deuceYou = False
	deuceOpp = False
	advYou = False
	advOpp = False
	deuceEnd = False
	point = random.randint(0, 100)

	while(deuceEnd == False):
		if((youStart == True and counter % 2 == 0) or (youStart == False and counter % 2 != 0)):
			if(point <= yourProb):
				advYou = False
				advOpp = False
				deuceYou = True
				print("You won 40 All")
				point = random.randint(0, 100)

				if(point <= yourProb):
					advYou = True
					print("You won Ad-In")
				else:
					advOpp = True
					deuceYou = False
					print("Opponent won Ad-In")
			else:
				advYou = False
				advOpp = False
				deuceOpp = True
				print("Opponent won 40 All")
				point = random.randint(0, 100)

				if(point <= yourProb):
					advYou = True
					deuceOpp = False
					print("You won Ad-Out")
				else:
					advOpp = True
					print("Opponent won Ad-Out")
		elif((youStart == True and counter % 2 != 0) or (youStart == False and counter % 2 == 0)):
			if(point <= oppProb):
				advYou = False
				advOpp = True
				deuceOpp = True
				print("Opponent won 40 all")
				point = random.randint(0, 100)

				if(point <= oppProb):
					advOpp = True
					print("Opponent won Ad-In")
				else:
					advYou = True
					deuceOpp = False
					print("You win Ad-In")
			else:
				advYou = False
				advOpp = False
				deuceYou = True
				print("You won 40 All")
				point = random.randint(0, 100)

				if(point <= oppProb):
					advOpp = True
					deuceYou = False
					print("Opponent won Ad-Out")
				else:
					advYou = True
					print("You won Ad-Out")
		point = random.randint(0, 100)

		if(deuceYou == True and advYou == True):
			scoreYou += 1
			deuceEnd = True
		elif(deuceOpp == True and advOpp == True):
			scoreOpp += 1
			deuceEnd = True

def tiebreaker():
	y_point = 0
	o_point = 0

	youStartTie = False
	oppStartTie = False

	yServe = False
	oServe = False

	endTiebreaker = False

	y_counter = 0
	o_counter = 0

	global youStart
	global counter
	global yourProb
	global oppProb

	global gameScoreYou
	global gameScoreOpp

	if((youStart == True and counter % 2 == 0) or (youStart == False and counter % 2 != 0)):
		youStartTie = True
	elif((youStart == True and counter % 2 != 0) or (youStart == False and counter % 2 == 0)):
		oppStartTie = True

	while(endTiebreaker == False):
		#beginning point
		if(youStartTie == True):
			point = random.randint(0, 100)
			if(point <= yourProb):
				y_point += 1
				oServe = True
				yServe = False
				youStartTie = False
			else:
				o_point += 1
				oServe = True
				yServe = False

		if(oppStartTie == True):
			point = random.randint(0, 100)
			if(point <= oppProb):
				o_point += 1
				yServe = True
				oServe = False
				oppStartTie = False
			else:
				y_point += 1
				yServe = True
				oServe = False
				oppStartTie = False

		#You are serving

		while(yServe == True):
			point = random.randint(0, 100)
			if(point <= yourProb):
				y_point += 1
				y_counter += 1
			else:
				o_point += 1
				y_counter += 1

			if(y_counter % 2 == 0):
				yServe = False
				oServe = True

			if((y_point >= 7) and (y_point - o_point >= 2)):
				gameScoreYou += 1
				yServe = False
				endTiebreaker = True
			if((o_point >= 7) and (o_point - y_point >= 2)):
				gameScoreOpp += 1
				yServe = False
				endTiebreaker = True

		#Opponent is serving

		while(oServe == True):
			point = random.randint(0, 100)
			if(point <= oppProb):
				o_point += 1
				o_counter += 1
			else:
				y_point += 1
				o_counter += 1

			if(o_counter % 2 == 0):
				yServe = True
				oServe = False

			if((y_point >= 7) and (y_point - o_point >= 2)):
				gameScoreYou += 1
				oServe = False
				endTiebreaker = True
			if((o_point >= 7) and (o_point - y_point >= 2)):
				gameScoreOpp += 1
				oServe = False
				endTiebreaker = True

if __name__ == '__main__':
	print("Welcome to your tennis match! Let's begin with the coin toss")
	coinToss = input("Enter 0 for Heads or 1 for Tails: ")

	x = random.randint(0, 1)
	print("Coin toss was: ", x)

	if(int(coinToss) == x):
		print("Congrats! You start serving")
		youStart = True
	else:
		print("Sorry, you serve second")
		youStart = False

	userProbYou = input("Enter a number from 0 to 100, this will serve as your probability that you win a serve: ")
	userProbOpp = input("Now enter a number from 0 to 100, this will serve as your opponent's probability to win a serve: ")

	yourProb = int(userProbYou)
	oppProb = int(userProbOpp)

	endSet = False
	endMatch = False

	while(endMatch == False):
		set()

		if((setScoreYou == 2 and setScoreOpp == 0) or (setScoreYou == 2 and setScoreOpp == 1)):
			print("You won the match")
			print(str(setScoreYou) + " - " + str(setScoreOpp))
			endMatch = True
		elif((setScoreOpp == 2 and setScoreYou == 1) or (setScoreOpp == 2 and setScoreYou == 1)):
			print("Your opponent won the match")
			print(str(setScoreYou) + " - "+ str(setScoreOpp))
			endMatch = True
