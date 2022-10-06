import turtle
import random

# sets background
bg = turtle.Screen()
bg.bgcolor("black")

# Bottom Line 1
turtle.penup()
turtle.goto(-170,-180)
turtle.color("white")
turtle.pendown()
turtle.forward(350)

# Mid Line 2
turtle.penup()
turtle.goto(-160,-150)
turtle.color("white")
turtle.pendown()
turtle.forward(300)

# First Line 3
turtle.penup()
turtle.goto(-150,-120)
turtle.color("white")
turtle.pendown()
turtle.forward(250)

# Cake
turtle.penup()
turtle.goto(-100,-100)
turtle.color("white")
turtle.begin_fill()
turtle.pendown()
turtle.forward(140)
turtle.left(90)
turtle.forward(95)
turtle.left(90)
turtle.forward(140)
turtle.left(90)
turtle.forward(95)
turtle.end_fill()

# Candles
turtle.penup()
turtle.goto(-90,0)
turtle.color("red")
turtle.left(180)
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(-60,0)
turtle.color("blue")
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(-30,0)
turtle.color("yellow")
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(0,0)
turtle.color("green")
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(30,0)
turtle.color("purple")
turtle.pendown()
turtle.forward(20)

# Decoration
colors = ["red", "orange", "yellow", "green", "blue", "purple", "black"]
turtle.penup()
turtle.goto(-40,-50)
turtle.pendown()

for each_color in colors:
    angle = 360 / len(colors)
    turtle.color(each_color)
    turtle.circle(10)
    turtle.right(angle)
    turtle.forward(10)
bday = "Happy Birthday Amma-Angel!" 
# Happy Birthday message
turtle.penup()
turtle.goto(-150, 50)
turtle.color("yellow")
turtle.pendown()
turtle.color('yellow')
style = ('Courier', 30, 'italic')
turtle.write('             Happy Birthday to our dear\n                 Amma-Angel !!', font=style, align='center')
turtle.hideturtle()
#turtle.write(bday, None, None, "24pt bold")
turtle.color("black")


# print("\nWelcome to the Tresure Hunt game!\nI will give you clue and that will lead you to the treasure map.\nWhen you have the treasure map then that will lead to the surprise!")

# while True:
# 	clue = input("\nYour first clue to find the treasure map is 'wheels at entrance'. Type 'c' to continue: ").lower()
# 	if clue == "c":
# 		break
# 	else:
# 		print("Please try again")
# while True:
# 	trace = input("\nOpen the tresure map and follow the trace. If you found the surprise the type the code word on the map to continue further: ").lower()
# 	if trace == "clockwork":
# 		print("Correct!")
# 		break
# 	else:
# 		print("Wrong! Please try again")	

# while True:
# 	like = input("Do you like the surprise amma ? Type 'yes' or 'no': ").lower()

# 	if like == "yes":
# 		print("Thank you amma! We have more surprises after one hour.")
# 		break
# 	elif like == "no":
# 		print("Ok amma.")
# 		break
# 	else:
# 		print("Please try again.")	


