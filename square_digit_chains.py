def get_sum_of_squared_digits(number_as_string_list):
  sum_of_squared_digits = 0
  for digit in number_as_string_list:
    sum_of_squared_digits += int(digit) ** 2
  return sum_of_squared_digits

def hits_eighty_nine(number_in_question):
  number_as_string = str(number_in_question)
  number_as_list_of_strings = list(number_as_string)
  sum_of_squared_digits = get_sum_of_squared_digits(number_as_list_of_strings)
  if sum_of_squared_digits == 89:
    return True
  elif sum_of_squared_digits == 1:
    return False
  else:
    return hits_eighty_nine(sum_of_squared_digits)

def count_number_of_eighty_nines(upper_number):
  count = 0
  for i in range(1, upper_number):
    if hits_eighty_nine(i):
      count += 1
  return count

print(count_number_of_eighty_nines(10000000))
