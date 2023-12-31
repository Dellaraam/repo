import sys
import random

#maybe two different lists. 
#One for the # of days 
#One fore the # of people
#maybe a double loop that takes 2 numbers and compares matches 

calender = int(sys.argv[1]) #calendar days  
people = int(sys.argv[2]) #people's birthdays

iterations = 1000 # number of cycles 
match = 0 #number of matching birthdays
for i in range(iterations):
	#create people with random birthdays 
	classroom = [] 
	for j in range(people): #range of people
		classroom.append(random.randint(1, calender)) #random birthdays in people
	
	shared = False 
	for m in range(people): 
	#range of people with bdays
		for n in range(m+1, people): 
		#compares bdays
			if classroom[m] == classroom[n]: 
				shared = True 
				break 
	if shared: match += 1

calender = int(sys.argv[1])  
people = int(sys.argv[2]) 

iterations = 1000 
match = 0

for i in range(iterations):

	cal = [0]*calender 
	
	shared = False 
	for j in range(people): #range of people
		bday = random.randint(1, calender) #random birthdays in people
		cal[bday-1] += 1
		if cal[bday-1] > 1:
			shared = True
			break
	if shared: match += 1


print(match/iterations)
