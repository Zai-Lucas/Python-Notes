# how to replace items in a list

mystery = list("halloween")
guessList = list("_________")

guess = input("Guess a letter")

index = 0
for letter in mystery:
	if letter == guess:
		guessList[index] = guess
	index += 1

print(guessList)