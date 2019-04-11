# Author: Robert Galloway
# Date: 10/04/2019

def minMultiple(n):
    for i in range(10,20):
        if (n % i != 0):
            return False
    return True


# Main Program
n = 20
while True:
    if(minMultiple(n)):
        break
    else:
        n+=20
print n
