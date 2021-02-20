# Problem 7

# By listing the first six prime numbers: 
# 2, 3, 5, 7, 11, and 13, we can see that the 
# 6th prime is 13.

# What is the 10 001st prime number?

# whichprime = 6
whichprime = 10001

import primeness

print('Prime #%d is %d.' % 
	(whichprime, primeness.first_n_primes(whichprime)[whichprime-1]))
