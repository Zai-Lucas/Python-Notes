# Make a list
myClasses = ["Algebra","English","World History"]
print(myClasses)

# Add an item to the list
# Append or insert
# Append wll add to the back of the list
myClasses.append("Coding")
print(myClasses)
favClass = input("What is your favorite class? ")
myClasses.append(favClass)
print(myClasses)
# Insert
myClasses.insert(3, "Art")
print(myClasses)
# Overwrite
myClasses[4] = "Science"
print(myClasses)

# Remove list items
# Remove, pop
# Remove will remove a specific item (have to tell which one to take out)
myClasses.remove("Science")
print(myClasses)
# Removing a non-existant item will create an error

# Pop will remove the item at a specific index
myClasses.pop()# pop without number will erase the last item
print(myClasses)
myClasses.pop(2)
print(myClasses)
# len - it returns the length of a list
print("myClasses is " + str(len(myClasses)) + " items long")


print(myClasses[len(myClasses) - 1]) # minus one needed to detect the 3rd number not a imaginary number

# loop through a list 
count = 1
for aClass in myClasses:
	print("Item " + str(count) + " is " + aClass)
	count = count + 1 # counts down the list

numbers = [4, 2, 5, 7, 8, 1, 9, 3]
# Challenge: loop through the list, add the numbers, and print the sum
point = 1
for number in numbers:
	point += number

print(point)
myClasses.append("cooking")

if "cooking" in  myClasses:
	print("Have fun cooking")
else:
	print("OK then")