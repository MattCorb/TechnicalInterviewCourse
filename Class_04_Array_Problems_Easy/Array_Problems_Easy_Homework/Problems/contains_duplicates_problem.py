# Given an array of integers, find if the array contains any duplicates
# Your function should return false if every element is distinct.
# This problem came from leetcode.com

input_array = [1, 2, 3, 4, 4]
# Output = True
# Brute Force

# def distinct(x):
#     output = {}
#     print(output.keys())
#     for i in x:
#         if i in output.keys():
#             output[i] += 1 
#         else:
#             output[i] = 1
#     conclusion = False
#     for i in output.values():
#         if i >= 2 :
#             conclusion = True
#             break
#     return conclusion

# Optomized  

def distinct(x):
    output = False
    hold = 0
    for i in range(len(x)):
        hold = x[0]
        x.pop(0)
        if hold in x:
            output = True
            break
    return output



print(distinct(input_array))