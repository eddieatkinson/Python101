known_primes = [2]

def is_prime(n, known_primes_list):
  for prime in known_primes_list:
    if n % prime == 0:
      return False
  return True

def sum_primes_below_n(n, known_primes_list, sum_of_primes):
  for i in range(3, n + 1):
    if is_prime(i, known_primes_list):
      known_primes_list.append(i)
      sum_of_primes += i
  return sum_of_primes

print(sum_primes_below_n(2000000, known_primes, 2))