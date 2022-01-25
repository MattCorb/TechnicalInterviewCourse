# Search an array of numbers to find a target number using binary search.
# The function should return the index of the target number if the target number is found
# or a -1 if the target is not found in the array.

# input_array = [ 1, 2, 5, 9, 12, 15, 21, 28,99, 100, 117]
# input_target = 0
# # Output = 2

# def biTree(x,t):
#     lower = 0
#     upper = len(x) - 1
#     while lower <= upper:
#         mid = int((upper + lower) / 2)
#         if x[mid] == t:
#             return mid     
#         elif x[mid] < t:
#             lower = mid + 1
            
#         elif x[mid] > t:
#             upper = mid - 1
#     return -1

# print(biTree(input_array,input_target))

# def MeAndZach(x,t):
#     lower = 0
#     upper = len(x) -1
#     while lower <= upper:
#         mid = int((upper + lower) / 2)
#         if x[mid] == t:
#             return mid
#         elif x[mid] < t:
#             lower = mid + 1
#         elif x[mid] > t:
#             upper = mid -1
#         return -1


def classbi(x):
    min = x[0]
    for i in x:
        if i < min:
            min = i
    return min

# print(classbi([3,4,5,6,1,2]))

def zachscrazyidea(x):
    lower = x[0]
    upper = x[-1]
    left = ((len(x) - 1) ) //2
    right = ((len(x)) )  // 2 

    while x[lower] < x[upper]:
        if x[left] < x[right]:
            left = upper - left // 2
            right = upper - right // 2 + 1
        elif x[left] > x[right]:
            return right

# print(zachscrazyidea([3,4,5,6,1,2]))

def mattscrazyidea(x):
    lower = 0
    upper = len(x) -1
    while lower < upper:
        mid = (upper + lower) // 2
        if x[mid] < x[lower]:
            upper = mid - 1
        else:
            lower = mid
    return x[upper]

# print(mattscrazyidea([3,4,5,6,1,2]))

def pleasehelpmezach(x):
    output = []
    for i, n in enumerate(x):
        hold = 1
        for j in range(0, len(x)):
            if j != i:
                hold = x[j] * hold 
        output.append(hold)
    return output

print(pleasehelpmezach([1,2,3,4]))
