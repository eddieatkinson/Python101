count = 0
more_coins = True
while more_coins:
	print "You have %d coins. Would you like another (Y or N)? " % count
	response = raw_input("> ")
	if response == "Y":
		print "Great!"
		count += 1
	else:
		print "Ok. Bye!"
		more_coins = False
