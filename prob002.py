# Problem 2
# Each new term in the Fibonacci sequence is generated 
# by adding the previous two terms. 
# By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence 
# whose values do not exceed four million, find the sum 
# of the even-valued terms.

fib = 0
a = 1
b = 2

sum_evens = b
limit = 4000000

while fib < limit:
	fib = a + b
	if fib <= limit:
		if not(fib%2):
			sum_evens += fib
	a = b
	b = fib

print('The sum of even Fibonacci elements not exceeding {0} is {1}.'.format(limit,sum_evens))
# The sum of even Fibonacci elements not exceeding 4000000 is 4613732.
