# def minMax(x):
#     min = x[0]
#     max = x[0]
#     for i in range(0,len(x)):
#         if x[i] > max:
#             max = x[i]
#         elif x[i] < min:
#             min = x[i]
#     return max, min

# print(minMax([0,1,2,3,4,5,0,10,1,-1,]))

# def reverse(x):
#     output = []
#     for i in range(0,len(x)):
#         output.append(x[-1])
#         x.pop(-1)
#     return output

# print(reverse([0,1,2,3,4,5,0,10,1,-1,]))


# def missingNO(x):
#     for i in range(0,len(x)):
#         if x[i] + 1 != x[ i + 1]:
#             return x[i] + 1
       
# print(missingNO([0,2,3,4,5,6,7]))

def end(x):
    for i in range(0,len(x)):
        if x[i] < 0:
            hold = x.pop(i)
            x.append(hold)
    return x
print(end([0,-2,3,-4,5,-6,7]))