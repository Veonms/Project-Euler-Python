# Author: Robert Galloway
# Date: 04/08/2019

val = 1
total = 0

for j in range(1000):
    val = val*2

size = str(val)

for i in range(len(size)):
    total += int(size[i])

print total
