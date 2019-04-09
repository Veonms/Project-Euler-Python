# Author: Robert Galloway
# Date: 09/04/2019

def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i

    return n

# Main Function
print largest_prime_factor(600851475143)
