# Problem 5
# 2520 is the smallest number that can be divided 
# by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is 
# evenly divisible by all of the numbers from 1 to 20?

# limit = 10
limit = 20
candidate = limit
found = False

while found == False:
	for div in range(2,limit):
		if candidate % div != 0:
			# print(candidate,'not divisible by',div)
			candidate += limit
			break
	else:   # note this else clause relates to the for loop
		print(candidate)
		found = True
