import time
import random



print("\nWelcome to the credits app! You can store your hours of credits,\n remove some of the credits,\nand you can add some of your credits!")

while True:
	choice = input("Type 'a' to add credits or type 's' to show your credits and type 'r' to remove some credits or 'q' to quit: ").lower()
	
	if choice == "a":
		w = input("Which credit you want to change. 1-'games' or 2-'movies': ") 
		if w == "1":
			number1 = int(input("Type the number of hours you want to add: "))
			print("Loading...")
			time.sleep(1)

			w = open("game_credits.txt", "r")
			num = str(int(w.read()) + int(number1))
			k = open("game_credits.txt", "w")
			k.write(num)
			k.close()



		elif w == "2":	
			number1 = int(input("Type the number of hours you want to add: "))
			print("Loading...")
			time.sleep(1)

			w = open("movie_credits.txt", "r")
			num = str(int(w.read()) + int(number1))
			k = open("movie_credits.txt", "w")
			k.write(num)
			k.close()
		else:
			print("Sorry, I did not understand what you were trying to chose")	
		

		


		print("Added the number of hours to credits....Done!")


	elif choice == "r":
		
		g = input("Which credit do you want to remove ? 1- games, 2-movies: ")
		if g == "1":


			number2 = int(input("Type the number of hours you want to remove: "))
			print("Removing...")

			w = open("game_credits.txt", "r")

			num = str(int(w.read()) - int(number2))
			k = open("game_credits.txt", "w")
			k.write(num)
			k.close()

			time.sleep(1)
			print("Done!")

		elif g == "2":
			number2 = int(input("Type the number of hours you want to remove: "))
			print("Removing...")

			
			w = open("movie_credits.txt", "r")

			num = str(int(w.read()) - int(number2))
			k = open("movie_credits.txt", "w")
			k.write(num)
			k.close()

			time.sleep(1)
			print("Done!")

		else:
			print("Sorry I didn't understand what to want to chose.")		

	elif choice == "s":
		print("Your game credits is..")

		w = open("game_credits.txt", "r")
		print(w.read())
		
		print("Your movie credits is..")

		w = open("movie_credits.txt", "r")
		print(w.read())

				

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


	
