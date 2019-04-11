# Author: Robert Galloway
# Date: 11/04/2019

def collatz(n, count=1):
    while n > 1:
        count += 1
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1
    return count

# Main Program
max = [0,0]
for i in range(1000000):
    chain = collatz(i)
    if chain > max[0]:
        max[0] = chain
        max[1] = i

print "Starting number: %s\nChain: %s" % (max[1],max[0])
