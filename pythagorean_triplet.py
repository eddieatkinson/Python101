def three_numbers_that_sum_to_n(n):
  for a in range(1, n + 1):
    for b in range(1, n + 1):
      if (a < b) & (a + b < n):
        c = n - a - b
        if ((a < c) & (b < c)):
          if (a**2 + b**2 == c**2):
            product = a*b*c
            return product

print(three_numbers_that_sum_to_n(1000))