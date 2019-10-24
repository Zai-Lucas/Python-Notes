# Making strings into lists
myString = "Arizona"
myList = list(myString)
print(myList)
secret = []
# Create list with underScores instead of letters
for a in myList:
	secret.append("_")
print(secret)

# how to replace an underscore with a letter
secret[2] = "i"
print(secret)