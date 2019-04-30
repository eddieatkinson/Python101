def find_sum_of_digit_n_powers(n):
  sum_of_everything_that_qualifies = 0
  for i in range(2, 1000000):
    i_as_string = str(i)
    sum_of_digits = 0
    for each_digit in i_as_string:
      sum_of_digits += int(each_digit)**n
    if sum_of_digits == i:
      sum_of_everything_that_qualifies += i
  return sum_of_everything_that_qualifies

print(find_sum_of_digit_n_powers(5))