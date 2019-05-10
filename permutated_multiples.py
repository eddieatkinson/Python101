def get_number_as_sorted_list_of_digits(n):
  n_as_list = list(str(n))
  n_as_list.sort()
  return n_as_list

def check_if_digits_are_the_same(n):
  two_n = 2 * n
  three_n = 3 * n
  four_n = 4 * n
  five_n = 5 * n
  six_n = 6 * n
  n_as_list = get_number_as_sorted_list_of_digits(n)
  two_n_as_list = get_number_as_sorted_list_of_digits(two_n)
  three_n_as_list = get_number_as_sorted_list_of_digits(three_n)
  four_n_as_list = get_number_as_sorted_list_of_digits(four_n)
  five_n_as_list = get_number_as_sorted_list_of_digits(five_n)
  six_n_as_list = get_number_as_sorted_list_of_digits(six_n)
  if n_as_list == two_n_as_list == three_n_as_list == four_n_as_list == five_n_as_list == six_n_as_list:
    return True
  else:
    return False

i = 0
same_digits = False
while not same_digits:
  i += 1
  same_digits = check_if_digits_are_the_same(i)

print(i)
