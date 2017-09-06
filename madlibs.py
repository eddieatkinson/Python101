adj = raw_input("Name an adjective: ")
animal = raw_input("Name an animal: ")
place = raw_input("Name a place: ")
num = int(raw_input("Pick a number: "))
print """I would love to have a %s pet %s. I would make sure I bring it the
next time I go to %s. Actually, I would love to have %d of them!""" % (adj, animal, place, num)