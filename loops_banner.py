user_input = raw_input("What would you like us to put a banner around? ")
# print "*" * (len(user_input) + 4)
# print "* " + user_input + " *"
# print "*" * (len(user_input) + 4)

for i in range(1, 4):
	if (i == 1 or i == 3):
		print "*" * (len(user_input) + 4)
	else:
		print "* " + user_input + " *"
