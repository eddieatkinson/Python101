import random
my_random_number = random.randint(1,10)
guess = 11
count = 5
print "I'm thinking of a number between 1 and 10."
while my_random_number != guess and count >= 0:
	if (count == 0):
		print "You ran out of guesses!"
		break
	print "You have %d guesses left." % count
	print "What's the number?"
	guess = int(raw_input("> "))
	if (guess > my_random_number):
		print "%d is too high. Try again!" % guess
	elif (guess < my_random_number):
		print "%d is too low. Try again!" % guess
	else:
		print "You win!"
		print "Would you like to play again (Y or N)?"
		play_again = raw_input("> ")
		if (play_again == "N"):
			print "Bye!"
		else:
			print "Great!"
			count = 6 # Sets count 1 above num guesses, to be decremented ln 28
			guess = 11 # Resets the guess out of range
			my_random_number = random.randint(1,10) # Creates a new random number
	count = count - 1