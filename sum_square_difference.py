def sum_of_squares(range_min, range_max):
  total = 0
  for i in range(range_min, range_max + 1):
    total += i
  return total**2
def square_of_sums(range_min, range_max):
  total = 0
  for i in range(range_min, range_max + 1):
    total += i**2
  return total

sum_squares = sum_of_squares(0, 100)
square_sums = square_of_sums(0, 100)

sum_square_difference = sum_squares - square_sums
print(sum_square_difference)
