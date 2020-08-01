import random

# Database of european countries in a list.
countries = ['ANDORRA', 'AUSTRIA', 'ALBANIA', 'BELARUS', 'BELGIUM', 'BULGARIA', 'BOSNIA AND HERZEGOVINA', 'CROATIA', 'CZECH REPUBLIC', 'CYPRUS', 'DENMARK', 'ESTONIA', 'FRANCE', 
'FINLAND', 'GERMANY', 'GREECE', 'HUNGARY','ICELAND', 'IRELAND', 'ITALY', 'KOSOVO', 'LITHUANIA', 'LATVIA', 'LUXEMBOURG', 'LIECHTENSTEIN', 'MACEDONIA', 'MONTENEGRO', 'MONACO', 
'MALTA', 'MOLDOVA', 'NORWAY', 'NETHERLANDS', 'PORTUGAL', 'POLAND', 'RUSSIA', 'ROMANIA', 'SPAIN', 'SAN MARINO', 'SERBIA', 'SWEDEN', 'SLOVENIA', 'SLOVAKIA', 'SWITZERLAND', 'TURKEY', 'UNITED KINGDOM', 'UKRAINE', 'VATICAN CITY']


length = len(countries) - 1
completed_problems = []
correct = 0
q = 0

print("\nGuess the European Country.\n")

while q < 12:

	# Randomly select a country for user to guess and check it has not already been asked.
	active = True
	while active:
		i = random.randint(0, length)
		if countries[i] not in completed_problems:
			problem  = countries[i]
			active = False

	# Remove half the letters of the string
	k = int(len(problem)/2)
	problem_array = []
	numbers = []

	# Convert string into characters
	a = 0
	while a < (len(problem)):
		problem_array.append(problem[a])
		a += 1
	
	# Get a random set of numbers which will be used to hide the relevant indices of the country name
	h = 0
	while h < k:
		r = random.randint(0, len(problem)-1)
		if r not in numbers:
			numbers.append(r)
			h+=1


	# Generate country with letters being replaced with '_' for user to guess
	for number in numbers:
		if problem[number] != ' ':
			problem_array[number] = '_'

	p = ' '.join(problem_array)
	print(f"{p}\n")

	# User input to see if response is same as country
	response = input("Answer: \n")
	if response.lower() == problem.lower(): 
		print("\nCorrect!\n")
		completed_problems.append(problem)
		correct += 1
	else:
		print("\nIncorrect!\n") 
		print(f"The correct answer is {problem}\n")
		completed_problems.append(problem)

	q += 1

# print final scores outside of loop with message.
if correct == q:
	print(f"Well done! You got {correct} out of {q}!\n")
elif correct >= (q - int(q/2)) and correct <= (q-1):
	print(f"Good effort! You got {correct} out of {q}.\n")
else:
	print(f"Poor effort! You only got {correct} out of {q}. Must try harder!\n") 