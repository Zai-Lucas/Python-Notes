#How to check if 1 number is a multiple of another

num = int(input("What number to check: "))

print("Checking  Number... ")

if num % 3 == 0:
	print("Your number is a multiple of three")
else:
	print("Your number isn't a multiple of three")

if num % 5 == 0:
	print("Your number is a multiple of five")
else:
	print("Your number isn't a multiple of five")



# How to print without new lines
print("Fizz")
print("Buzz")

# Same line
print("Fizz", end="")
print("Buzz")


