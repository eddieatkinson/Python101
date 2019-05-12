def number_of_digits_equals_power(n, power):
  n_as_string = str(n**power)
  if len(n_as_string) == power:
    return True
  return False

# def get_number_of_n_digit_nums_of_nth_power(n, power):

number_that_qualify = 0
for base in range(1, 10):
  for power in range(1, 300):
    if number_of_digits_equals_power(base, power):
      number_that_qualify += 1

print(number_that_qualify)
