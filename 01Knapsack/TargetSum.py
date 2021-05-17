# 7. Target Sum

def countTargetSum(arr, subset1Sum, n):
    for j in range(subset1Sum+1):
        t[0][j] = 0

    for i in range(n+1):
        t[i][0] = 1

    for i in range(1, n+1):
        for j in range(1, subset1Sum+1):
            if arr[i-1] > j:
                t[i][j] = t[i-1][j]

            else:
                t[i][j] = t[i - 1][j - arr[i - 1]] + t[i - 1][j]

    return t[n][subset1Sum]

arr = [1,1,2,3]
targetSum = 1
n = len(arr)
arrSum = sum(arr)
subset1Sum = int((targetSum+arrSum)/2)
t= [[0 for j in range(subset1Sum +1)] for i in range(n+1)]

print(subset1Sum)
print(countTargetSum(arr, subset1Sum, n))