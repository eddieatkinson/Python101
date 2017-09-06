# CONDITIONALS
# == - compare left and right
# === - compare left and right AS WELL AS data type
# 16 == "16" 	True
# 16 === "16"	False
if(16 == 16):
	print "True"
if(16 == "16"):
	print "False"
#if(16 == "16"): # same
#	print "False"

if(1 == 2):
	print "True"

if(1==2):
	print "True!"
elif(2 == 2):
	print "Second one is true!"
else:
	print "False!"

classSize = 19;
question = "How big is your class?";
response = raw_input("> ")
# Remember, raw input is always collected as a string
response_as_an_int = int(response)
if(response_as_an_int != classSize):
	print "You must not be in the Sept class."
else:
	print "You're with me!"

# Random is a python module, that comes with python.
import random;
rand_number = random.randint(1,10)
print rand_number
# # Loops
# A while loop will run forever or until the condition is false
keep_going = True
while keep_going:
	get_answer = raw_input("Please hit any key")
	keep_going = False
print "You are out of the loop!"