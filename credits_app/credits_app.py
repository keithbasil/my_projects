import time
import random


# Creating the welcome screen
print("\nWelcome to the credits app! You can store your hours of credits,\n remove some of the credits,\nand you can add some of your credits!")

# Checking what the user will choose 
while True:
	choice = input("Type 'a' to add credits or type 's' to show your credits and type 'r' to remove some credits or 'q' to quit: ").lower()

	# If user chosen a(add)	
	if choice == "a":
		w = input("Which credit you want to change. 1-'games' or 2-'movies': ")

		# if user chosen 1(games)

		if w == "1":
			number1 = int(input("Type the number of hours you want to add: "))
			print("Loading...")
			time.sleep(1)

			# Adding credit to the file "game_credits.txt"

			w = open("game_credits.txt", "r")
			num = str(int(w.read()) + int(number1))
			k = open("game_credits.txt", "w")
			k.write(num)
			k.close()


		# If user chosen 2 (movie)

		elif w == "2":	
			number1 = int(input("Type the number of hours you want to add: "))
			print("Loading...")
			time.sleep(1)

			# Adding credit to file "movie_credits.txt"

			w = open("movie_credits.txt", "r")
			num = str(int(w.read()) + int(number1))
			k = open("movie_credits.txt", "w")
			k.write(num)
			k.close()


		else:
			print("Sorry, I did not understand what you were trying to chose")	
		

		


		print("Added the number of hours to credits....Done!")


	# If user chosen r (remove)

	elif choice == "r":
		
		g = input("Which credit do you want to remove ? 1- games, 2-movies: ")

		# if user chosen 1(games)

		if g == "1":


			number2 = int(input("Type the number of hours you want to remove: "))
			print("Removing...")

			w = open("game_credits.txt", "r")
			
			# Removing credits from file "game_credits.txt"

			num = str(int(w.read()) - int(number2))
			k = open("game_credits.txt", "w")
			k.write(num)
			k.close()

			time.sleep(1)
			print("Done!")

		# if user chosen 2(movie)

		elif g == "2":
			number2 = int(input("Type the number of hours you want to remove: "))
			print("Removing...")

			
			w = open("movie_credits.txt", "r")

			# Removing credits from file "movie_credits.txt"

			num = str(int(w.read()) - int(number2))
			k = open("movie_credits.txt", "w")
			k.write(num)
			k.close()

			time.sleep(1)
			print("Done!")

		else:
			print("Sorry I didn't understand what to want to chose.")		

	# if user chosen s (show)

	elif choice == "s":
		print("Your game credits is..")

		w = open("game_credits.txt", "r")
		print(w.read())
		
		print("Your movie credits is..")

		w = open("movie_credits.txt", "r")
		print(w.read())

	# If user chosen q (quit)				

	elif choice == "q":
		bye = ["Thank you for using the app! Bye!", "See you next time! :)", "Bye! Bye!", """
				   _	   
               _  / |
              / \ | | /)
               \ \| |/ /
                \ Y | /___
              .-.) '. `__/
             (.-.   / /
                 | ' |
                 |___|
                [_____]
        Bye!    |     |"""]
		print(random.choice(bye))
		break
	else:
		print("Sorry, I didn't understand what you were trying to say. Please try again. ")
