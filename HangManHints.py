myWord = "hello"

choice = input("Type a word: ")

if choice == myWord:
	print("It's a match")
else:
	print("Not a match")

# how to check if a letter is in a word
letter = input("Type a letter")
if letter in myWord:
	print("Letter is in the word")
else:
	print("Letter is not in the word")

count = 0
for s in myWord:
	if s == letter:
		print(count)
	count += 1