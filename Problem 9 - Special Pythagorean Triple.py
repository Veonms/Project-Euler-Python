# Author: Robert Galloway
# Date: 11/04/2019

def isPythagTriple(a,b,c):
    if(a**2 + b**2 != c**2):
        return False
    return True

# Main Program
for a in range(1,1000):
    for b in range(1,1000):
        c = ((1000 - a) - b) # As a<b<c
        if(a<b<c):
            if(isPythagTriple(a,b,c)):
                print(a*b*c)
