# You are given a string s and an integer array indices of the same length. 
# The string s will be shuffled such that the character at the ith position 
# moves to indices[i] in the shuffled string. Return the shuffled string.

# Input: s = "codeleet", indices = [4,5,6,7,0,1,2,3]
# Output: "leetcode"

input_string = "ttbdisschoeee"
indices = [7, 9, 3, 10, 4, 5, 0, 8, 11, 2, 12, 6, 1]
# v = ['s','o','','b','i','s','e','t','h','t','d','h','e']
def rearrange(s,indices):
    hold = []
    for i in range(0,len(s)):
        hold.append([s[indices[i]]])
    newString = ''
    for i in range(len(hold)):
        newString += hold[i][0]
    return newString
 
print(rearrange(input_string,indices)) 

# Optimized

# def rearrange(s,indicies):
#     output = ''
#     for i in range(len(s)):
#         output += s[indicies[i]]
#     return output
# print(rearrange(input_string,indices))
