def get_proper_divisors(n):
  proper_divisors = []
  for i in range(1, n):
    if n % i == 0:
      proper_divisors.append(i)
  return proper_divisors

def deficient_or_abundant(n):
  sum_of_proper_divisors = sum(get_proper_divisors(n))
  if sum_of_proper_divisors > n:
    return 'abundant'
  elif sum_of_proper_divisors < n:
    return 'deficient'
  else:
    return 'perfect'

def get_all_abundant_numbers_through_n(n):
  abundant_numbers = []
  for i in range(12, n + 1):
    if (deficient_or_abundant(i) == 'abundant'):
      abundant_numbers.append(i)
  return abundant_numbers

def get_all_numbers_that_are_not_sum_of_two_abundant_numbers_through_n(n):
  abundant_numbers_list = get_all_abundant_numbers_through_n(int((n + 1) / 2))
  all_numbers_that_are_not_sum_of_two_abundant_numbers = []
  for i in range(24, n + 1):
    is_not_sum_of_two_abundant_numbers = True
    for abundant_number in abundant_numbers_list:
      if i - abundant_number in abundant_numbers_list:
        is_not_sum_of_two_abundant_numbers = False
    if is_not_sum_of_two_abundant_numbers:
      all_numbers_that_are_not_sum_of_two_abundant_numbers.append(i)
  return sum(all_numbers_that_are_not_sum_of_two_abundant_numbers)

print(get_all_numbers_that_are_not_sum_of_two_abundant_numbers_through_n(28123))
