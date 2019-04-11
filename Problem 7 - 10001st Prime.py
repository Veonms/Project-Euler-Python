# Author: Robert Galloway
# Date: 11/04/2019


def isPrime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# returns the nth prime number
def nthPrime(n):
    numberOfPrimes = 0
    i = 1

    while numberOfPrimes < n:
        i += 1
        if isPrime(i):
            numberOfPrimes += 1
    return i

# Main Program
print(nthPrime(10001))
