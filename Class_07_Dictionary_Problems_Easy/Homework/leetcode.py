# def myPower( x: float, n: int) -> float:
#     out = abs(x)
#     if n == 0:
#         out = 1
#     elif n < 0:
#         for i in range(1,abs(n)):
#             out  *= abs(x)
#         out = 1 /out
#     else:
#         for i in range(0, n -1):
#             out *= x
#     if (out < 0 and n % 2 == 0) or (out > 0 and n % 2 == 1 and x < 0) :
#         out *= -1 
#     return out
# # print(myPow(34.00515,-3))

# def myPow(x,n):
#     if n == 0:
#         return 1
#     elif n < 0:
#          return myPow(x,n +1) / x
#     elif n > 0:
#         return myPow(x,n -1) * x
# print(myPow(2,-3))

# def majorityElement(x):
#     out = {}

#     for i in x:
#         if i in out.keys():
#             out[i] += 1
#         else:
#             out[i] = 1
    
#     for i in out.keys():
#         if out[i] > len(x) / 2:
#             return i
        

# print(majorityElement([2,2,2,2,3,2,6]))

def twoSum(x,t):
    out = {}
    for i, j in enumerate(x):
        out[j] = i

    for i in out.keys():
        help = t - i
        if help in out.keys():
            return out[help],out[i]


# print(twoSum([2,7,11,15],26)) 

def twoSumsagain(x,t):
    out = {}
    for i,j in enumerate(x):
        help = t - x[i]
        if help in out.keys(): return(out[help],i)
        else:
            out[j] = i

def uwords(s1,s2):
    s3 = f'{s1} {s2}'
    wordArr = s3.split(" ")
    out = {}

    for i in wordArr:
        if i in out.keys():
            del out[i]
        else:
            out[i] = 1

    return out.keys()

print(uwords("this apple is sweet","this apple is sour"))
