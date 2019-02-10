import math

def get_factors(n):
  number_of_factors = 2
  for i in range(2, round(math.sqrt(n)) + 1):
    if n % i == 0:
      if n / i != i:
        number_of_factors += 2
      else: number_of_factors += 1
  return number_of_factors

def find_triangle_with_at_least_n_factors(n):
  number_of_factors = 0
  traingle_number = 1
  number_to_add = 2
  while number_of_factors < n:
    traingle_number += number_to_add
    number_to_add += 1
    number_of_factors = get_factors(traingle_number)
  return traingle_number

print(find_triangle_with_at_least_n_factors(500))
