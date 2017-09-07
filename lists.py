# student1 = "Milayla"
# student2 = "Jennifer"
# student3 = "Nikolas"
# student4 = "Zach"

# print student1
# print student2
# print student3
# print student4
# # The above is tedious and takes a lot of code. Use a LIST!

# # A list is a single variable with a bunch of numbered (indexed) parts.
# # An index, in a list, is ALWAYS a number (integer), and starts at 0.
# # A list is made with []. Every element is separated by a ,.
# students = [
# 	"Mikayla",
# 	"Jennifer",
# 	"Nikolas",
# 	"Zach"
# ]

# print students
# print students[0]
# print students[3]
# print students[-1] # prints last element

atlanta_teams = [
	"Falcons",
	"Braves",
	"Hawks",
	"Thrashers",
]

# print atlanta_teams
# # Remove an element from the end with "pop()"
# atlanta_teams.pop()
# print atlanta_teams
# # We have another team: ATL United!
atlanta_teams.append("ATL United") # adds to the end what's in the ()
print atlanta_teams

# for i in range(0,5):
atlanta_teams_length = len(atlanta_teams)
for i in range(0,atlanta_teams_length):
	# check to see if the ith element (the one we're on) is Thrashers
	if(atlanta_teams[i] == "Thrashers"):
		thrashers_index = i
		# break means stop the loop. I don't care about the conditio
		break

atlanta_teams.pop(thrashers_index)
print atlanta_teams


# atlanta_teams.pop(1) # can specify which element to remove in pop(i)
# print atlanta_teams

# Split turns a string into a list.
# It expects a "Delimiter", which is what it's supposed to use to break up the elements in the string.
teams_as_a_string = "Falcons, Braves, Hawks, ATL United"
print teams_as_a_string
teams_as_a_list = teams_as_a_string.split(',')
print teams_as_a_list

# Lists also have a sort method.
# Beware, sort will change the list.
# atlanta_teams.sort() # Alphabetical
# print atlanta_teams

# Sorted will sort the list but will not change the list.
# Instead, it returns the sorted list, which you can assign to a variable.
sorted_atlanta_teams = sorted(atlanta_teams)
print atlanta_teams
print sorted_atlanta_teams

sorted_atlanta_teams.reverse() # Will reverse the order
print sorted_atlanta_teams

# If you want to copy a portion of the list, you can use [x:y]
# This will create a copy of the array. It will NOT change the original.
# It will start at the xth element, and will stop at the yth (won't include yth).
# So if we want Braves and Hawks (1, 2) we start at 1, we stop before 3.
baseball_basketball = atlanta_teams[1:3]
print baseball_basketball

all_but_the_first = atlanta_teams[1:] # Copies the 1th through the end.
print all_but_the_first
# all_but_the_first = atlanta_teams[1:len(atlanta_teams)] # same thing as above

# If you want to delete an index, you can use the remove method.
# Alternative to pop, you provide the string, not the element.
atlanta_teams.remove("Braves")
print atlanta_teams

# insert... we can insert an element wherever we want
atlanta_teams.insert(1,"Braves")
print atlanta_teams

