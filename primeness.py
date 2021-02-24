import math

primes = [2,3]

def extend_primes(upto):
    """Pre-extend the table of known primes"""
    for candidate in range(primes[-1]+2, upto + 1, 2):
        if isprime(candidate):
          # print "appending ",candidate
          primes.append(candidate)

def is_prime(x):
    print('This function does not work as advertised.')
    print('checking',x)
    print('\tprimes:',primes)
    """Check whether "x" is a prime number"""
    # Check for too small numbers
    if x < primes[0]:
        return False
    # Calculate the largest possible divisor
    max = int(math.sqrt(x))
    # First, check against known primes
    for prime in primes:
        if prime > max:
            return True
        if x % prime == 0:
            return False
    # Then, lazily extend the table of primes as far as necessary
    for candidate in range(primes[-1], max + 1, 2):
        if is_prime(candidate):
            primes.append(candidate)
            print('\t\tappend',candidate)
            if x % candidate == 0:
                return False
    return True

def isprime(n):
  if n<=1:
    return False
  if n<4:
    return True
  if n % 2 == 0:
    return False
  if n < 9:
    return True
  if n % 3 == 0:
    return False

  div = 5
  while div <= int(math.sqrt(n)):
    if n % div == 0:
      return False
    if n % (div+2) == 0:
      return False
    div += 6
  return True


def primefactor(n):
  if n > primes[-1]:
    extend_primes(n)

  # print('primes:',primes)

  stop = n
  factors = []
  for prime in primes:
    if prime > stop:
      break
    while n%prime == 0:
      factors.append(prime)
      n /= prime
  return factors

def first_n_primes(n):
  inc = 2
  while(len(primes)<n):
    extend_primes(primes[-1]+inc)
    inc += 1
  return primes[0:n]

def prime_sieve(n):
  limit = int(math.sqrt(n))
  sieve = [True] * n
  sieve[0] = sieve[1] = False
  for i in range(4,n,2):
    sieve[i] = False
  for i in range(3,limit+1,2):
    if sieve[i]:
      for j in range(i*i, n, 2*i):
        sieve[j] = False
  return sieve
