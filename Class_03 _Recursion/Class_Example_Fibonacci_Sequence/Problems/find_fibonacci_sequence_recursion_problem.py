# Write a program that creates a portion of the fibonacci sequence recursively

# def fibseq(n):
#     if n == 0 or n == 1:
#         return n
#     else:
#         return fibseq(n - 1) + fibseq(n-2)

# print(fibseq(1))
def pal(x):
    if len(x) == 0 or len(x) == 1:
        return True
    elif(x[0] == x[len(x)]):
        x.pop(0)
        x.pop(len(x))
        pal(x)


print(pal('tacocat'))
