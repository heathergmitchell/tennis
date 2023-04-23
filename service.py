class serve:

	def serve():
		print("This player serves")


class deucetry():
	def deuce2():
		while(deuceA !=2 or deuceB!=2):
			if (point <= 50):
				print("player A point")
				deuceA +=1
			else:
				print("player B point")
				deuceB += 1
			point = random.randint(0,100)
		if (deuceA == 2):
			print("player A wins deuce")

		else:
			print("player B wins deuce")

class deuce:
	def deuce():
		while(deuceA != 2 or deuceB != 2):
			if(counter % 2 == 0):   #Player A serving
				if(point <= 50):	#Player A won the point
					deuceA +=1
					print(lineup[0] + " vs. " + lineup[1])
					print("Advantage In")
				else: #Player A lost point
					deuceB += 1
					print(lineup[0] + " vs. " + lineup[1])
					print("Advantage Out")
					if(deuceA != 0):
						deuceA -=1
			else: #Player B serving
				if(point > 50):      #Player B won point
					deuceB += 1
					print(lineup[0] + " vs. " + lineup[1])
					print("Advantage In")
				else:   #Player B lost point
					deuceA +=1
					print(lineup[0] + " vs. " +  lineup[1])
					print("Advantage Out")
					if (deuceB != 0):
						deuceB -= 1
			point = random.randint(0,100)
			print(point)

		if(deuceA == 2):
			print(point)
			print(lineup[0] + " won first game")
			print("Ad vs. " + score[scoreB])
		elif(deuceB == 2):
			print(point)
			print(lineup[1] + " won first game")
			print(score[scoreA] + " vs. Ad")
			point = random.randint(0,100)
			print(point)
		return;
