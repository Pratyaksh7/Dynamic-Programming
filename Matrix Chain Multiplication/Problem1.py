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

    if t[i][j] != -1:
        return t[i][j]

    else:
        mn = maxsize
        for k in range (i, (j-1)+1):
            tempAns = solve(arr,i,k) + solve(arr, k+1, j) + (arr[i-1] * arr[k] * arr[j])

            if tempAns < mn:
                mn = tempAns

        t[i][j] = mn
    return t[i][j]

arr = [40, 20, 30, 10, 30]
i = 1
j = len(arr) - 1

t = [[-1 for _ in range(len(arr))] for _ in range(len(arr))]

print(solve(arr,i,j))

