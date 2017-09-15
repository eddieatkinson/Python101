pal_list = []
# num_digits = int(raw_input("How many digits would you like to test? "))
# for i in range (10^(num_digits - 1), 10^(num_digits)):
# 	for j in range (10^(num_digits - 1), 10^(num_digits)):
for i in range (100, 1000):
	for j in range (100, 1000):
		product = i * j
		num_string = str(product)
		num_list = list(num_string)
		num_list_copy = num_list
		if num_list == num_list[::-1]:
			# print num_list
			prod_string = "".join(num_list)
			prod_int = int(prod_string)
			pal_list.append(prod_int)
sorted_pal_list = sorted(pal_list)
print max(sorted_pal_list)