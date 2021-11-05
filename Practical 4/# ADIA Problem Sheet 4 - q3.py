# ADIA Problem Sheet 4 - q3
# binary search

A = [-5, 4, 5, 6, 21, 30, 32, 38, 40, 42, 52, 58, 61, 62]
find = 52

i, j = 0, len(A)-1
counter = 0

while j-i >= 0:
    counter +=1
    print(A[i:j])
    
    pivot = ((j-i)//2)+i
    print(pivot)
    
    if A[pivot] > find:
        j = pivot-1
    elif A[pivot] < find:
        i = pivot+1
    else:
        print("pivot found at:\n", pivot)
        break
    
print("counter", counter)

# complexity: O(logn)
        
