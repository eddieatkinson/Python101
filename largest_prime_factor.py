# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?
known_primes = [2, 3]
def is_prime(n):
  number_of_primes = len(known_primes)
  for i in range(number_of_primes):
    if n % known_primes[i] == 0:
      return False
    else:
      continue
  known_primes.append(n)

def prime_list_builder(max_tested):
  for i in range(4, max_tested + 1):
    is_prime(i)

prime_list_builder(13195)
print(known_primes)
