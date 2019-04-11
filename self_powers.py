def find_power_of_number_n_plus_all_lesser_powers(n):
  sum_of_powers = 0
  for i in range(1, n + 1):
    sum_of_powers += i**i
  return sum_of_powers

number_to_test = int(input('Number to test? '))
numbers_from_end = int(input('How many from the end? '))
power_sum = find_power_of_number_n_plus_all_lesser_powers(number_to_test)
power_sum_as_string = str(power_sum)
length_of_string = len(power_sum_as_string)
last_n_digits = power_sum_as_string[length_of_string - numbers_from_end:]
print(last_n_digits)
