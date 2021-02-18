# Problem 4
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 
# 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of 
# two 3-digit numbers.

digits = 3

x = 10**digits
y = 10**digits
largest = 0

for i in range(x,int(x/10),-1):
	for j in range(y,int(y/10),-1):
		prod = i*j
		if str(prod) == str(prod)[::-1] and prod > largest:
			largest = prod

print('The largest palindromic product of two',digits,'digit numbers is',largest,'.')
