# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of 
# the number 600851475143 ?

import math
import primeness

# candidate = 13195
candidate = 600851475143

for n in reversed(range(2, int(math.sqrt(candidate))+1)):
	if candidate % n == 0:
		if primeness.isprime(n):
			print(n,'is the largest prome factor of',candidate,'.')
			break
