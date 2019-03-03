def sum_of_digits(power):
  result = 2 ** power
  result_as_string = str(result)
  result_as_list = list(result_as_string)
  sum_of_digs = 0
  for num in result_as_list:
    sum_of_digs += int(num)
  return sum_of_digs

print(sum_of_digits(1000))
