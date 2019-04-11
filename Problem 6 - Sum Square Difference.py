# Author: Robert Galloway
# Date: 10/04/2019

def sumOfSquares():
    total = 0
    for i in range(101):
        total+= (i**2)
    return total


def squareOfSums():
    num = 0
    for i in range(101):
        num += i
    total = num**2
    return total

# Main Program
print(squareOfSums() - sumOfSquares())
