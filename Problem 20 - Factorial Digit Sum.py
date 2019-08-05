# Author: Robert Galloway
# Date: 04/08/2019



def fac(n):
    j = n
    for i in range(n-1):
        j -= 1
        n = n * j
    return n

#Main Program
sum = 0
for h in str(fac(100)):
    sum += int(h)
print sum
