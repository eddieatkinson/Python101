minimum_number_that_contains_all = 1
one_through_ten = 1
increment = 0

while one_through_ten < 21:
  if minimum_number_that_contains_all % one_through_ten != 0: # minimum number is not evenly divisible
    minimum_number_that_contains_all += increment # we increment up the minimum number by itself
  else: # minimum number is evenly divisible, so we increment the one through ten
    increment = minimum_number_that_contains_all
    one_through_ten += 1
print(minimum_number_that_contains_all)