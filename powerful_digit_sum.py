def get_sum_of_digits(number):
  sum_of_digits = 0
  number_as_string = str(number)
  number_as_list = list(number_as_string)
  for digit in number_as_list:
    sum_of_digits += int(digit)
  return sum_of_digits

def get_maximum_digit_sum(upper):
  maximum_digit_sum = 0
  for i in range(1, upper):
    for j in range(1, upper):
      power = i**j
      digit_sum = get_sum_of_digits(power)
      if digit_sum > maximum_digit_sum:
        maximum_digit_sum = digit_sum
  return maximum_digit_sum

print(get_maximum_digit_sum(100))
