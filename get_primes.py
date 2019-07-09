import sys

args = sys.argv

loops = args[1]

def is_prime(num, l):
	for i in range(1, len(l)):
		if num % l[i] == 0:
			return False
	return True


# [1, 2, 3, 5, 7]

# 11 % 1 != 0
# 11 % 2 != 0
# 11 % 3 != 0
# 11 % 5 != 0
# 11 % 7 != 0




def get_primes(loops=int(loops)):
	primes = set([1])

	for i in range(1, loops):
		if is_prime(i, list(primes)):
			primes.add(i)

	print(primes)

get_primes()