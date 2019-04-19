fib_list = [1, 1]

def get_next_in_fib_sequence(current_fib_list):
  next_in_fib_sequence = current_fib_list[-2] + current_fib_list[-1]
  current_fib_list.append(next_in_fib_sequence)
  return next_in_fib_sequence

less_than_1000_digits = True

while less_than_1000_digits:
  next_in_fib_sequence = get_next_in_fib_sequence(fib_list)
  if len(str(next_in_fib_sequence)) > 999:
    less_than_1000_digits = False
    print(len(fib_list))