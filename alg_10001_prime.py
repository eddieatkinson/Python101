# known_primes = []

# def is_prime(n):
# 	total_primes = len(known_primes)
# 	for i in range (0, total_primes):
# 		if (n % known_primes[i] == 0):
# 			# Not prime!
# 			return False
# 		else:
# 			continue
# 	known_primes.append(n)
# 	return True

# def nth_prime(n):
# 	for i in range (2, n * 15):
# 		if len(known_primes) < n:
# 			is_prime(i)
# 		else:
# 			break
# 	print max(known_primes)

# nth = int(raw_input("Which prime would you like? "))
# nth_prime(nth)

known_primes = [2]
# number_to_test = 3

def is_prime(primes_list, n):
  for prime in primes_list:
    if n % prime == 0:
      return False
  return True

def determin_nth_prime(n, number_to_test):
  while len(known_primes) < (n + 1):
    if is_prime(known_primes, number_to_test):
      known_primes.append(number_to_test)
    number_to_test += 1
  print(known_primes[n - 1])

# print(known_primes)
determin_nth_prime(10001, 3)
