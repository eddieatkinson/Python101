# Guess the number! Hint. It's 5.
secret_number = 5
guess = 2 # Ensures the while loop runs
print "I'm thinking of a number between 1 and 10."
while secret_number != guess:
	print "What's the number?"
	guess = int(raw_input("> "))
	if (secret_number != guess):
		print "Please try again"
	else:
		print "You win!"