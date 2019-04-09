# Author: Robert Galloway
# Date: 09/04/2019

num = 0

for i in range(1000):
    if (i%3 == 0) or (i%5 == 0):
        num = num + i

print("Total: ",num)
