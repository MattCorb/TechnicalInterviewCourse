# You are given an m x n integer grid accounts where accounts[i][j]
# is the amount of money the ith customer has in the jth bank.
# Return the wealth that the richest customer has.
# A customer's wealth is the amount of money they have in all their bank accounts. 
# The richest customer is the customer that has the maximum wealth.

input_accounts = [[2,8,7],[7,1,3],[1,9,5]]
# Output: 17

# def rich(x):
#     total = 0
#     output = []
#     for i in range(len(x)):
#         for j in range(len(x)):
#            total += x[i][j] 

#         if len(output) == 0:
#             output.append(total)
#         elif output[0] < total:
#             output[0] = total
#         total = 0
#     return output[0]
# print(rich(input_accounts))

# Optimize

def rich(x):
    richest = 0
    for i in range(len(x)):
        if sum(x[i]) > richest:
            richest = sum(x[i])
    return richest
print(rich(input_accounts))