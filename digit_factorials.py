import math

def is_curious_number(n):
  number_as_string = str(n)
  sum_of_digits = 0
  for digit in number_as_string:
    sum_of_digits += math.factorial(int(digit))
  if sum_of_digits == n:
    return True
  else:
    return False

sum_of_curious_numbers = 0
for i in range(3, 100000):
  if is_curious_number(i):
    sum_of_curious_numbers += i

print(sum_of_curious_numbers)