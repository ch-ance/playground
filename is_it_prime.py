import sys

args = sys.argv

number = args[1]

def is_prime(num=int(number)):
	# If number is even, it's not prime
	if num % 2 == 0:
		print(f'{num} is not prime')


is_prime()