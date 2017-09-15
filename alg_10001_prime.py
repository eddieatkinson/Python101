known_primes = []

def is_prime(n):
	total_primes = len(known_primes)
	for i in range (0, total_primes):
		if (n % known_primes[i] == 0):
			# Not prime!
			return False
		else:
			continue
	known_primes.append(n)
	return True

def nth_prime(n):
	for i in range (2, n * 15):
		if len(known_primes) < n:
			is_prime(i)
		else:
			break
	print max(known_primes)

nth = int(raw_input("Which prime would you like? "))
nth_prime(nth)