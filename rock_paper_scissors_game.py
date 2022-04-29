import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to Rock, Paper and Scissors Game! You can type 'q' for quit if you want to exit the game. Let the games start!")

game_images = [rock, paper, scissors]

points = 0

computer_points = 0

while True:
	choice = input("What do you choose ? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

	if choice == "q":
		bye = ["Ok then, Bye Bye! See you soon!", "Bye! Have a good day!", "Bye! I will see you next time!"]
		bye_choice = random.randint(0, 2)
		print(bye[bye_choice])
		break


	choice_int = int(choice)

	computer_choice_int = random.randint(0, 2)

	if choice_int >= 3 or choice_int < 0:
		print("You chose an invalid number. Try again")

	else:		

		if choice_int == 0:
			print("You chose:\n")
			print(game_images[0])
		elif choice_int == 1:
			print("You chose:\n")
			print(game_images[1])
		elif choice_int == 2:
			print("You chose:\n")
			print(game_images[2])	

		if computer_choice_int == 0:
			print("\nComputer chose:\n")
			print(game_images[0])
		elif computer_choice_int == 1:
			print("\nComputer chose:\n")
			print(game_images[1])	
		else:
			print("\nComputer chose:\n")
			print(game_images[2])	


	if computer_choice_int == choice_int:
		print("It's a draw. That means we get no points. Oh no!")
	elif computer_choice_int == 0 and choice_int == 1:
		print("You win! Super! Paper covers rock.")
		points += 5
		print(f"Your score is {points}, and my score is {computer_points}.\n")

	elif computer_choice_int == 0 and choice_int == 2:
		print("You lose. Next time, let's hope you will win. Rock wins agaist scissors.")
		computer_points += 5
		print(f"Your score is {points}, and my score is {computer_points}.\n")

	elif computer_choice_int == 1 and choice_int == 0:
		print("You lose. Try again in the next round. Paper covers rock.")
		computer_points += 5
		print(f"Your score is {points}, and my score is {computer_points}.\n")

	elif computer_choice_int == choice_int:
		print("It's a draw. No!")
	elif computer_choice_int == 1 and choice_int == 2:
		print("You win! Great job! Scissors turns paper into tiny bits.")
		points += 5	
		print(f"Your score is {points}, and my score is {computer_points}.\n")

	elif computer_choice_int == 2 and choice_int == 0:
		print("You Win!. Rock crushes scissors.")
		points += 5
		print(f"Your score is {points}, and my score is {computer_points}.\n")

	elif computer_choice_int == 2 and choice_int == 1:
		print("You lose. Scissors beats paper.")
		computer_points += 5
		print(f"Your score is {points}, and my score is {computer_points}.\n")

	elif computer_choice_int == choice_int:
		print("It's a draw.")	
			


