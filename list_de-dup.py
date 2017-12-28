in_list = [1, 3, 3, 3]
dup_list = in_list[0:]
dup_list2 = in_list[0:]
# print dup_list
# new_list = []
for i in range (0, len(in_list)):
	for j in range (0, len(in_list)):
		if (j < i and in_list[i] == dup_list[j]):
			dup_list2.pop(i)
print dup_list2

