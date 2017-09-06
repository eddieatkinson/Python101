# print "Hello, World"
# print("Hello, World")
# print """
# Triple quotes
# 	are here
# 	to
# 	stay!
# """
# name = "Eddie Atkinson" #This is a string

# # Data types
# # strings - English stuff, for people to read.
# # numbers - something with digits and the stuff that goes with them (- or . or e)
# # floats, integers:
# # 	-- float has a . in it
# # 	-- integer - has no -
# # Booleans - True or False, 1 or 0, off or on
# # list - list of things. A single variable with a bunch of like parts
# # dictionary - variable of variable
# # objects - we will deal with this later
# name = "Eddie " + "Atkinson" # + is a concatenate symbol with strings
# first = "Eddie"
# last = "Atkinson"
# full_name = first + " " + last
# print full_name
# meaning_of_life = 40 + 2 # + is now an addition symbol
# forty_two = 84 / 2
# forty_two = 21 * 2
# one = 83 % 2
# # Python cannot concatenate a string and a number
# print "-" * 20

# # By argument
# first_name = "Eddie"
# last_name = "Atkinson"

# # Intermingle english and vars: way 1
# print "Hello {} {}".format(first_name, last_name)
# # way 2
# print "Hello %s" % "You!"

# # Floats
# pi = 3.14
# print type(pi)
# makeMeAnInt = int(pi)
# print makeMeAnInt
# print type(makeMeAnInt)

# # Booleans
# the_truth = True
# print type(the_truth)

# addOneToMe = 1
# addOneToMe = addOneToMe + 1
# # addOneToMe++ does not work in Python
# addOneToMe += 1
# addOneToMe -= 1

# # Order of operations!
# () overrides everything, so use them!
print "What is your name?"
name = raw_input(">")
print "Your name is %s" % name

print "What is your age?"
age = int(raw_input(">"))
print "Your age is %d" % age