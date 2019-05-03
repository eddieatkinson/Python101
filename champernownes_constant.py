constant = ''
i = 1

def create_constant_of_length_n(n, string, increment):
  while len(string) < n + 1:
    string += str(increment)
    increment += 1
  return string

def find_product_of_different_digits(n1, n2, n3, n4, n5, n6, n7, string, increment):
  const = create_constant_of_length_n(n7, string, increment)
  prod = int(const[n1 - 1]) * int(const[n2 - 1]) * int(const[n3 - 1]) * int(const[n4 - 1]) * int(const[n5 - 1]) * int(const[n6 - 1]) * int(const[n7 - 1])
  return prod

print(find_product_of_different_digits(1, 10, 100, 1000, 10000, 100000, 1000000, constant, i))
