for i in range (2520, 300000000, 2520):
	divisible = True
	while divisible == True:
		for j in range (11, 21):
			if i % j == 0: # evenly divisible
				if j == 20:
					print i
					quit()
				else:
					continue

			else:
				divisible = False
				break		