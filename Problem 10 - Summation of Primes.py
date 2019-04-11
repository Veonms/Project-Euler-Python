# Author: Robert Galloway
# Date: 11/04/2019

def isPrime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Main Program
primeTotal = 0

for i in range(2000000):
    if(isPrime(i)):
        primeTotal+= i

print primeTotal
