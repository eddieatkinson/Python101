# Guess the random number.
import random
my_random_number = random.randint(1,10)
guess = 11
print "I'm thinking of a number between 1 and 10."
while my_random_number != guess:
	print "What's the number?"
	guess = int(raw_input("> "))
	if (guess > my_random_number):
		print "%d is too high. Try again!" % guess
	elif (guess < my_random_number):
		print "%d is too low. Try again!" % guess
	else:
		print "You win!"