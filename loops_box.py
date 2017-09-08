width = int(raw_input("Width? "))
height = int(raw_input("Height? "))
for i in range(1, height + 1):
	if(i == 1 or i == height):
		print "*" * width
	else:
		print "*" + " " * (width - 2) + "*"
		