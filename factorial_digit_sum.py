import math

def get_sum_of_numbers_in_list(list):
  sum_of_digs = 0
  for number in list:
    sum_of_digs += number
  return sum_of_digs

def get_factorial_digit_sum(factorial):
  factorial_as_string = str(factorial)
  factorial_as_list = list(factorial_as_string)
  factorial_as_list_of_numbers = []
  for digit_string in factorial_as_list:
    factorial_as_list_of_numbers.append(int(digit_string))
  sum_of_digs = get_sum_of_numbers_in_list(factorial_as_list_of_numbers)
  return sum_of_digs

number_for_factorial = int(raw_input('What number? '))

print(get_factorial_digit_sum(math.factorial(number_for_factorial)))