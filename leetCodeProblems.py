# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
from pyparsing import nums


def myPow(x,n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n == -1:
        return 1 / x
    res = myPow(x, n // 2)
    return res * res * (x if n % 2 == 1 else 1)
# print(myPow(x,n))
nums = [1,1,2]
cond = True
left = 0
right = 1
while cond == True:
    if nums[right] != '_':
        if nums[left] == nums[right] and right < len(nums):
            nums.pop(right)
            nums.append('_')           
        else:
            left +=1
            right += 1
    else:
        cond = False
        out = nums[:right]
        print(type(out))

