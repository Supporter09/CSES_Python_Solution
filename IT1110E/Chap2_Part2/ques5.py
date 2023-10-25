import math

# Function to generate all prime numbers up to n

def generatePrimes(n):
	# Create a boolean array "isPrime[0..n]" and initialize all entries as True
	isPrime = [True] * (n + 1)
	primes = []

	# A value in isPrime[i] will finally be False if i is Not a prime, else True.
	for i in range(2, n + 1):
		if isPrime[i]:
			# Append prime number to list
			primes.append(i)
			# Mark multiples of i as not prime
			for j in range(i * i, n + 1, i):
				isPrime[j] = False

	return primes

# Function to check if a prime number can be expressed as the sum of two prime numbers

def isPossible(n):
	# Generate all primes up to n
	primes = generatePrimes(n)

	# Iterate over all prime numbers
	for i in range(len(primes)):
		# Get the difference between n and the current prime number
		diff = n - primes[i]

		if diff < 2:
			break

		isDiffPrime = True
		# Check if the difference is a prime number
		for j in range(2, int(math.sqrt(diff)) + 1):
			if diff % j == 0:
				isDiffPrime = False
				break
		if isDiffPrime:
			return True
	return False


# Driver code
n = int(input())
for i in range(n):
	test = int(input())
	if isPossible(test):
		print("YES") # If n can be represented as the sum of two primes
	else:
		print("NO") # If n cannot be represented as the sum of two primes
