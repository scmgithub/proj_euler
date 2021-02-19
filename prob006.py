# Problem 6

# The sum of the squares of the first ten natural numbers is,
# 	1**2 + 2**2 + ... + 10**2 = 385

# The square of the sum of the first ten natural numbers is,
# 	( 1 + 2 + ... + 10 )**2 = 55**2 = 3025

# Hence the difference between the sum of the squares of 
# the first ten natural numbers and the square of the sum is 
# 	3025 − 385 = 2640.

# Find the difference between the sum of the squares of the
# first one hundred natural numbers and the square of the sum.

# nums = 10
nums = 100
sum = 0
sumOfSquares = 0 

for n in range(1,nums+1):
	sum += n
	sumOfSquares += n**2

squareOfSum = sum**2

print('The sum of the squares of the first %d natural numbers is %d.' % (nums, sumOfSquares))
print('The square of the sum of the first %d natural numbers is %d.' % (nums, squareOfSum))
print('The difference is %d.' % (squareOfSum-sumOfSquares))
