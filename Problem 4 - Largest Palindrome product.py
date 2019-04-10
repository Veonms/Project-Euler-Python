# Author: Robert Galloway
# Date: 10/04/2019

def isPalindrome(s):
     return s == s[::-1]

maxProduct = 0

for i in range(999, 900, -1): # All 3 digit numbers
    for j in range(i, 900, -1):
        product = i * j
        if isPalindrome(str(product)):
            maxProduct = max(maxProduct, product)
            
print maxProduct
