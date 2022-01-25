# Say you have an array for which the ith element is the price of a given stock on day i
# If you were only permitted to complete at most one transaction (i.e, buy one and 
# sell one share of the stock) design an algorithm to find the maximum profit
# This problem came from leetcode.com

input_array = [7, 1, 5, 3, 6, 4]
# Output = 5

# def profit(x):
#     output = []
#     for i in range(len(x)):
#         for j in range(len(x) - 1):
#             if len(output) == 0:
#                 output.append(x[i] - x[j + 1])
#             elif((x[i] - x[j + 1]) < output[0] ):
#                 output[0] = (x[i] - x[j + 1]) 
    
#     return output[0] * -1
# print(profit(input_array))

# Optimized Solution

def profit(x):
    topProfit = 0
    minPrice = x[0]
    for i in range(len(x)):
        if x[i] < minPrice:
            minPrice = x[i]
        if x[i] - minPrice > topProfit:
            topProfit = x[i] - minPrice
    return topProfit

        
print(profit(input_array))