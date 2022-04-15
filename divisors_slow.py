from timeit import default_timer as timer
import math

def divisors_of(n):
	d = []
	 # this method is really slow
	# for x in range(1,n+1):
	# 	# print('\tx:',x)
	# 	if n%x == 0:
	# 		d.append(x)

	#  this is somewhat better
	for x in range(1,int(math.floor(math.sqrt(n))+1)):
		if n%x == 0:
			d.append(x)
			if x != int(n/x):  # compensate for perfect squares (1,36,...)
				d.append(int(n/x))
	return d

count = 1
trxi = 0
divisors = 0
millions = 0

start = timer()

while divisors <= 500:
	tri += count
	if math.floor(tri/1000000) > millions:
		print('tri:',tri,'\telapsed time:',timer()-start,'seconds')
		millions = tri/1000000
	divs = divisors_of(tri)
	divisors = len(divs)
	count += 1

print(tri,'has',divisors,'divisors.')
print(count,'triangle numbers')
