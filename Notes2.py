#9/26
#Conditional
print("Welcome to the Ticket Bot")
print("You must be 18 to see R-rated Movies")
age = int(input("How old are you"))

if age > 17:
	print("You can see an R-rated Movie")

else:
	print("You cannot see an R-rated Movie")

print("Thanks")

mysteryNum = 6
guess = int( input("Guess a number between 1 and 10"))

if guess == mysteryNum:
	print("Good Guess, That's Correct")
elif guess > 10:
	print("Please Reread")
elif guess > mysteryNum:
	print("Too High")
else:
	print("Too Low")

# Conditional operators: <, >, >=, <=, == (is equal to), != (Not equal to),

birthday = input("Is today your birthday(yes/no): ")
if birthday == "yes":
	print("Happy Birthday")
elif birthday == "no":
	print("Hope you have a good day anyway")
else:
	print("Read") 