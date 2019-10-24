# how to keep track of misses
secret = "christmas"
misses = 0
secret = list(secret)

hangList = ['''pic 1''', ''' pic 2''',''' pic 3 ''', ''' pic 4''','''pic 5''','''pic6''', '''pic7''']

while misses < 7:
	print(hangList[misses])
	guess = input("Guess a letter: ")
	if guess in secret:
		#loop through secret and find all matching letters
		print("That letter is in the secret word")
	else:
		misses = misses + 1