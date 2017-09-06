amount = float(raw_input("What is the bill amount? "))
service = raw_input("How was your service (good, fair, or bad)? ")
num_people = int(raw_input("How many ways shall we split the check? "))
if (service == "good"):
	tip = .2 * amount
elif (service == "fair"):
	tip = .15 * amount
else:
	tip = .1 * amount
total = amount + tip
tip_rnd = round(tip, 2)
tot_rnd = round(total, 2)
per_person = total / num_people
per_rnd = round(per_person, 2)
print "Your tip amount is $%s and your total is $%s." % (tip_rnd, tot_rnd)
print "Your amount per person is $%s." % per_rnd
