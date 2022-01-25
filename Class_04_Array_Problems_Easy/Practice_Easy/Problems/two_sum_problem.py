# Given an array of integers, return indices of the two numbers such that they add up to a specific target
# You may assume that each input would have exactly one solution, and you may not use the same element twice
# This problem came from leetcode.com

input_array = [2, 5, 6, 3, 9] 
input_target = 9
# Output = [2, 3]

# def sum(ia,it):
#     output = []
#     for i in range(len(ia)):
#         for j in range(len(ia)-1):
#             if ia[i] + ia[j+1] == it:
#                 output.append(i)
#                 output.append(i+1)
#                 break
#         if len(output) == 2:
#             break

#     return output

# print(sum(input_array,input_target))

# optomized
def sum(ia,it):
    output = []
    for i in range(len(ia)):
        hold = (it - ia[i])
        if  hold in ia:
            output.append(ia[i])
            output.append((it - ia[i]))
            break
    return output
print(sum(input_array,input_target))
