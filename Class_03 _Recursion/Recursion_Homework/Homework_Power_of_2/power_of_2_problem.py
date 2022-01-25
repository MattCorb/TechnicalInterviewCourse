# Given an integer n, return True if it is a power of 2. 
# An integer n is a power of two, if there exists an integer x such that n == 2^x
def PowerFinder(n):
    if n == 1:
        return True
    elif n % 2 == 1 or n == 0:
        return False
    else:
        return PowerFinder(n/2)

print(PowerFinder(.5))
# Examples:

# Input: n = 4
# Output: True
# 2^2 = 4

# Input : n = 16
# Output : True
# 2^4 = 16

# Input : n = 13
# Output : False