import sys
import time

args = sys.argv

loops = args[1]

start_time = tim

def is_prime(num, ls):
	for i in range(1, len(ls)):
		if num in ls:
			return False
		if num % ls[i] == 0:
			return False
	return True


def get_primes(loops=int(loops)):
	primes = set([1])

	for i in range(1, loops):
		if is_prime(i, list(primes)):
			primes.add(i)

	print(primes)

get_primes()