from turtle import Turtle, Screen
import heroes
import time
import random


hero_name = heroes.gen()

print(f"I am {hero_name}! I shall draw a square, a dash line, a pattern and I will walk to make a bit of mess of art!")

time.sleep(3)

tim = Turtle()
tim.shape("square")
tim.color("firebrick3")

def draw_square():
	for _ in range(4):
		tim.forward(100)
		tim.right(90)

draw_square()

tim.penup()

tim.left(100)
tim.forward(200)

tim.shape("classic")
tim.color("grey")
tim.right(100)

def draw_dash():
	for _ in range(15):
		tim.pendown()
		tim.forward(10)
		tim.penup()
		tim.forward(10)

draw_dash()

tim.penup()
tim.left(180)
tim.forward(500)
tim.left(90)
tim.forward(200)

colors = ["blue", "lawn green", "medium violet red", "crimson", "chocolate", "gold", "yellow", "dim gray",
"steel blue", "dark cyan", "rosy brown", "LightSeaGreen", "IndianRed", "olive drab", "LightSalmon3", "LightCoral",
"HotPink4", "PeachPuff2", "peru", "plum2"]


def pattern():
	tim.pendown()
	tim.right(90)

	tim.color(random.choice(colors))
	for triangle in range(3):
		tim.forward(70)
		tim.right(-120)

	tim.color(random.choice(colors))
	for square in range(4):
		tim.forward(70)
		tim.right(-90)

	tim.color(random.choice(colors))
	for pentigon in range(5):
		tim.forward(70)
		tim.right(-72)

	tim.color(random.choice(colors))
	for _ in range(6):
		tim.forward(70)
		tim.right(-60)

	tim.color(random.choice(colors))
	for _ in range(7):
		tim.forward(70)
		tim.right(-51)

	tim.color(random.choice(colors))
	for _ in range(8):
		tim.forward(70)
		tim.right(-45)

	tim.color(random.choice(colors))
	for _ in range(9):
		tim.forward(70)
		tim.right(-40)


pattern()

directions = [0, 90, 180, 270]

tim.penup()
tim.left(180)
tim.forward(200)
tim.pendown()


tim.pensize(15)
tim.speed("fastest")

def random_walk():
	for _ in range(200):
		tim.color(random.choice(colors))
		tim.forward(30)
		tim.setheading(random.choice(directions))

random_walk()	



screen = Screen()
screen.exitonclick()
