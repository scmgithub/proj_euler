# Problem 1
#
# If we list all the natural numbers below 10 that are 
# multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

total = 0
div1 = 3
div2 = 5
limit = 1000

for n in range(1,limit):
	if not(n%div1) or not(n%div2):
		total += n

print('The sum of all multiples of {0} or {1} below {2} is {3}.'.format(div1,div2,limit,total))

# The sum of all multiples of 3 or 5 below 1000 is 233168.