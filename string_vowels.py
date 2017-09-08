print "Give me a string"
in_string = raw_input("> ")
upper_string = in_string.upper()
string_as_list = list(upper_string)
for i in range (1, len(string_as_list)):
	if (string_as_list[i] == "A" or string_as_list[i] == "E" or string_as_list[i] == "I" or string_as_list[i] == "O" or string_as_list[i] == "U"):
		if (string_as_list[i] == string_as_list[i-1]):
			vowel_extender = [string_as_list[i], string_as_list[i], string_as_list[i]]
			vowel_string = "".join(vowel_extender)
			string_as_list.insert(i + 1, vowel_string)
			i += 2
new_string = "".join(string_as_list)
print new_string