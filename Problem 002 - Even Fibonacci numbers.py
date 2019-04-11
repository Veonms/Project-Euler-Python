# Author: Robert Galloway
# Date: 09/04/2019


def Fibonacci(n):
    if(n<=1):
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

# Main Program
total = 0
i = 0

while Fibonacci(i)<4000000:
    if(Fibonacci(i)%2 == 0):
        total = total + Fibonacci(i)
    i+= 1

print total
