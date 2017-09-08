
# Lists are really really handy but are changeable. Mutations occur.
# What if you wanted something that couldn't be changed (immutible).
# A tuple is always a list except:
# 1. Its values cannot be changed
# 2. It uses () instead of []

# a_tuple = (1, 2, 3)
# print a_tuple
# print a_tuple[1]

# Dictionaries
# Dictionaries are just like lists, but instead of number indices,
# they have English indices.

# name = "Rob"
# gender = "Male"
# height = "Tall"

# A list makes no sense to tie them together...
# person = [
# 	"Rob",
# 	"Male",
# 	"Tall"
# ]

# person = {
# 	"name": "Rob",
# 	"gender": "Male",
# 	"height": "Tall"
# }

# print person["name"]
# print person["height"]

# zombie = {}
# zombie["weapon"] = "axe"
# zombie["health"] = 100
# zombie["speed"] = 10
# print zombie

# for key, value in zombie.items():
# 	print "Zombie has a key of %s with a value of %s" % (key, value)
# 	# print "Zombie has a key of %s with a value of %s" % (key, zombie[key]) This is the same.

# # Del will remove the key and value!
# del zombie["speed"]
# print zombie

# is_nighttime = True
# if (is_nighttime):
# 	zombie["health"] += 50

# put lists and dictionaries together!
zombies = [] # a list
zombies.append ({
	"speed": 10,
	"weapon": "fist",
	"name": "Joe"
})
zombies.append ({
	"speed": 15,
	"weapon": "bat",
	"name": "Willie",
	"victims": [
		"Jane",
		"Bill",
		"Harry"
	]
})

print zombies[1]["victims"][2]