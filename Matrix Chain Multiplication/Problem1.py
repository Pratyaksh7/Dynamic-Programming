# 1. Matrix Chain Multiplication Recursive

# total 4 steps:
# 1. find the correct value of i and j
# 2. find the base condition
# 3. find value of k for looping
# 4. calculate answer from temporary answers

from sys import maxsize
def solve(arr,i,j):
    if i >= j:
        return 0
    else:
        mn = maxsize
        for k in range (i, (j-1)+1):
            tempAns = solve(arr,i,k) + solve(arr, k+1, j) + (arr[i-1] * arr[k] * arr[j])

            if tempAns < mn:
                mn = tempAns
    return mn

arr = [40, 20, 30, 10, 30]
i = 1
j = len(arr) - 1

print(solve(arr,i,j))

