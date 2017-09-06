# Guess the number! Gives clues as to whether the guess is too high or too low.
secret_number = 5
guess = 2
print "I'm thinking of a number between 1 and 10."
while secret_number != guess:
	print "What's the number?"
	guess = int(raw_input("> "))
	if (guess > secret_number):
		print "%d is too high. Try again!" % guess
	elif (guess < secret_number):
		print "%d is too low. Try again!" % guess
	else:
		print "You win!"