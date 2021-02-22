# Problem 9
# A Pythagorean triplet is a set of three natural numbers, 
# a < b < c, for which,

# a**2 + b**2 = c**2
# For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

# There exists exactly one Pythagorean triplet for which 
# a + b + c = 1000.
# Find the product abc.

from timeit import default_timer as timer

total = 1000

start = timer()

for a in range(1,int((total/3))+1):
	for b in range(a,int((total/2))+1):
		c = total - a - b
		if a**2 + b**2 == c**2:
			print('a:',a,' b:',b,' c:',c)
			print("The product abc = %d." % (a*b*c))
			break
	else:
		continue

end = timer()
print ('Elapsed time:', end - start)
