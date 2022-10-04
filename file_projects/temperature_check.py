while True:
	temp_check = int(input("What is the temperature today ? "))


	def check_temp(temp):
		if temp < 15:
			print("It is going to rain, so bring an umbrella or a jacket.")
		elif temp > 25 and temp <= 35:
			print("Later today it is going to rain or it is becoming cold outside, so pack a jacket")
		elif temp < 35:
			print("Leave the jacket at home")	
		elif temp >= 36:
			print("It is sunny now, leave the jacket at home.")
		

	check_temp(temp_check)

	again = input("Do you want to try again ? Type 'y' or 'n'")