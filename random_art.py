from turtle import Turtle, Screen
import heroes
import random



# Creating a turtle

tim = Turtle()
tim.shape("square")
tim.color("firebrick3")


colors = ["blue", "lawn green", "medium violet red", "crimson", "chocolate", "gold", "yellow", "dim gray",
"steel blue", "dark cyan", "rosy brown", "LightSeaGreen", "IndianRed", "olive drab", "LightSalmon3", "LightCoral",
"HotPink4", "PeachPuff2", "peru", "plum2"]


directions = [0, 90, 180, 270]



tim.pensize(15)
tim.speed("fastest")

def random_walk():
	for _ in range(500)
		tim.color(random.choice(colors))
		tim.forward(30)
		tim.setheading(random.choice(directions))

random_walk()	



screen = Screen()
screen.exitonclick()
