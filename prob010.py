# Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

import primeness
from timeit import default_timer as timer

# limit = 10
limit = 2000000
sum = 0

start = timer()

# Sieve
primes = primeness.prime_sieve(limit)
for n in range(2,limit):
	if primes[n]:
		sum += n

# Factors
# for n in range(limit):
# 	if primeness.isprime(n):
# 		sum += n

print('The sum of the primes below %d is %d.' % (limit, sum))

end = timer()

print('Elapsed time:',end - start,'seconds')