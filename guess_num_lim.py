# Guess the number. You get 5 tries.
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
		print "%d is too high." % guess
	elif (guess < my_random_number):
		print "%d is too low." % guess
	else:
		print "You win!"
	count = count - 1