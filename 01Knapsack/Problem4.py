# 4. Count of subset sum with a given sum

def countSubset(arr, sum, n):
    for j in range(sum+1):
        t[0][j] = 0

    for i in range(n+1):
        t[i][0] = 1

    for i in range(1, n+1):
        for j in range(1, sum+1):
            if arr[i-1] > j:
                t[i][j] = t[i-1][j]

            else:
                t[i][j] = countSubset(arr, j-arr[i-1], i-1) + countSubset(arr, j, i-1)

    return t[n][sum]

arr = [2,3,5,6,8,10]
# how many subsets of this array are making the sum of 10
totalSum = 10
n = len(arr)

t = [[0 for j in range(totalSum+1)] for i in range(n+1)]
print(countSubset(arr, totalSum, n))