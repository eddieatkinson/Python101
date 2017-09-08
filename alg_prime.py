# def is_prime(n, prime_list):
# 	for i in prime_list:
# 		if (n % i == 0):
# 			return False 
# 	return True

# num = 600851475143
# # factor = []
# prime_factor = []
# for i in range (2, num):
# 	if (num % i == 0): # factor
# 		if is_prime(i, prime_factor):
# 			prime_factor.append(i)
		


# # 		factor.append(i)
# # for j in factor:
# # 	if is_prime(j):
# # 		prime_factor.append(j)
# # print factor
# print prime_factor
# if (len(prime_factor) > 0):
# 	print max(prime_factor)
# else:
# 	print "Your number %d is prime!" % num

# Create an array of known primes
known_primes = [2, 3]
def is_prime(n):
	total_primes = len(known_primes)
	for i in range (0, total_primes):
		if (n % known_primes[i] == 0):
			# Not prime!
			return False
		else:
			# It might be prime, it might not.
			# It's just not divisible by this number
			continue
	known_primes.append(n)
	return True
print is_prime(5)

