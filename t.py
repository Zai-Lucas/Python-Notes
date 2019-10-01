from turtle import *

myTurtle = Turtle()
screen = myTurtle.getscreen()

myTurtle.forward(50)

def writeName():
	name = screen.textinput("name box", "What is your name?")
	myTurtle.write(name, move=True, align="left", font=("Arial",30,"normal"))
	screen.listen()
def forward():
	myTurtle.forward(10)
def right():
	myTurtle.right(90)

screen.onkey(writeName, "w")
screen.onkey(forward, "Up")
screen.onkey(right, "Right")

screen.listen()

screen.mainloop()