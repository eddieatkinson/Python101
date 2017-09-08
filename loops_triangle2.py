height = int(raw_input("Height? "))
j = 1
for i in range (1, height + 1):
	print " " * (height - i) + "*" * (j)
	j += 2