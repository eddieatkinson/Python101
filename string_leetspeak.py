print "Give me a paragraph"
in_parag = raw_input("> ")
upper_parag = in_parag.upper()
parag_as_list = list(upper_parag)
for i in range (0, len(parag_as_list)):
	if (parag_as_list[i] == "A"):
		parag_as_list[i] = "4"
	elif (parag_as_list[i] == "E"):
		parag_as_list[i] = "3"
	elif (parag_as_list[i] == "G"):
		parag_as_list[i] = "6"
	elif (parag_as_list[i] == "I"):
		parag_as_list[i] = "1"
	elif (parag_as_list[i] == "O"):
		parag_as_list[i] = "0"
	elif (parag_as_list[i] == "S"):
		parag_as_list[i] = "5"
	elif (parag_as_list[i] == "T"):
		parag_as_list[i] = "7"
new_parag = "".join(parag_as_list)
print new_parag				