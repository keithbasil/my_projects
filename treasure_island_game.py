print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choice_1 = input("You have arrived the beach, there are two paths the left path is to the woods and the right one to the lighthouse. Which one do you chose left or right ?\n ").lower()

if choice_1 == "left":
	choice_2 = input("You reached the woods then you get lost suddely you see a house filled with candy on the left path and a spaceship on the right. Which one do you chose left or right ?\n ").lower()
	if choice_2 == "right":
		choice_3 = input("""You get inside the spaceship then suddenly you find aliens they chant then you feel sleepy when you wake up you see an alien city they take you to a throne room where the king alien tells you that you need to entertain his people then he will help you with whatever you to find. Type 'y' for yes or 'n' for no. \n""").lower()

		if choice_3 == "y":	
			choice_4 = input("After you entertain the aliens the king alien askes what you want, you tell you were send to find the hidden treasure. The king alien chant then you find yourself near the sea and a island on the middle he tells you that on the island is the treasure. You have two choices type 'wait' to wait for a boat or type 'swim' to swim across the sea.\n ").lower()

			if choice_4 == "wait":
				choice_5 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose ? ").lower()
				if choice_5 == "red":
					print("""""You entered the room of fire. Game over.
				     (  .      )
           )           (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^""")  
				elif choice_5 == "blue":
					print("""You found the tresure! You win!
			
			/\____;;___/
		| /         /
		`. ())oo() .
			|\(%()*^^()^/
		%| |-%-------|
		% \ | %  ))   |
		%  \|%________|""")

				elif choice_5 == "yellow":
					print("""You enter the room of beasts. Game Over. """)

				else:
					print("You chose a door that doent't exist. Game Over")

			else:
				print("You get attacked by a crocodile. Game Over")			

		else:
			print("The king alien puts you to jail. Game Over.")
									 


	else:
		print("""It is the house of the witch. Game Over.
		;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
		;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
		;;;;;;;;;;;;;;;;-' ___      '-;;;;;;;;;;;;;;;;
		;;;;;;;;;;;;-'    `'-.`'-.      '-;;;;;;;;;;;;
		;;;;;;;;;;'           )   `\       ';;;;;;;;;;
		;;;;;;;;'            /      \   ^V^  ';;;;;;;;
		;;;;;;;           __/________\__       ;;;;;;;
		;;;;;;  ^V^      '--/}}}}}}"}}--'       ;;;;;;
		;;;;;              {{{{{{  aa\__         ;;;;;
		;;;;;              }}}}} ,___ __}        ;;;;;
		;;;;;             {{{{{\  \_//           ;;;;;
		;;;;;              }}}}//'--u            ;;;;;
		;;;;;        _     .--'`U\               ;;;;;
		;;;;;   ::::| \   (   _,\\\              ;;;;;
		;;;;;;  ::::|  |===\  \\=\))=======D    ;;;;;;
		;;;;;;; ::::|_/     `> \\              ;;;;;;;
		;;;;;;;;.           /__//            .;;;;;;;;
		;;;;;;;;;;.         Y\_\\_         .;;;;;;;;;;
		;;;;;;;;;;;;-._                _.-;;;;;;;;;;;;
		;;;;;;;::;;;;;;-.          .-;;;;;;;;;;;;;;;;
		;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
		;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; """)

else:
	print("""Inside the lighthouse is a ghost. Game Over.
	
      .'``'.      ...
     :o  o `....'`  ;
     `. O         :'
       `':          `.
         `:.          `.
          : `.         `.
         `..'`...       `.
                 `...     `.
                     ``...  `.
                          `````.""")
