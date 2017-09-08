fib_first = [1, 2]
even_fib = []
i = 1
max_fib = 4000000
curr_sum = fib_first[1]
while curr_sum <= max_fib:
	if (curr_sum % 2 == 0):
		even_fib.append(curr_sum)
	curr_sum = fib_first[i] + fib_first[i-1]
	if (curr_sum > max_fib):
		break
	fib_first.append(curr_sum)
	i += 1
# print fib_first
# print even_fib[-1]
print sum(even_fib)

