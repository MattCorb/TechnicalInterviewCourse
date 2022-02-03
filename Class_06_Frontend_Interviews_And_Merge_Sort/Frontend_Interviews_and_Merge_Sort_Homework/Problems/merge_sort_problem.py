# Write a merge sort algorithm to sort an array. 
# The function should return the sorted array.

# two examples


# array1 = [45, 98, 3, 24, 15, 77, 9, 50] # output: [3, 9, 15, 24, 45, 50, 77, 98]
array2 = [18, 16, 27, 4, 12] # output: [4, 12, 16, 18, 27]

def merge(x):
    if len(x) > 1:
        mid = len(x) // 2
        left = x[:mid]
        right = x[mid:]
    
        merge(left)
        merge(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                x[k] = left[i]
                i += 1
            else:
                x[k] = right[j]
                j+= 1
            k += 1

        while i < len(left):
            x[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            x[k] = right[j]
            j += 1
            k += 1

# merge(array1)
# print(array1)

array1 = [1,2,3,3,3,3,3,2,1]
def MajorityElement(x):
    if len(x) > 1:
        mid = len(x) // 2
        left = x[:mid]
        right = x[mid:]

        MajorityElement(left)
        MajorityElement(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                x[k] = left[i]
                i += 1
            else:
                x[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            x[k] = left[i]
            k += 1
            i += 1
        
        while j < len(right):
            x[k] = right[j]
            j += 1
            k += 1
    

MajorityElement(array1)
print(array1[-3:])
out = 1
for i in array1[-3:]:
    out *= i

print(out)
