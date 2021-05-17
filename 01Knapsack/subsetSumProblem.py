# 2. Subset sum problem

def subset(arr, sum, n):
    for j in range(sum + 1):
        t[0][j] = False
    for i in range(n+1):
        t[i][0] = True

    for i in range(1, n+1):
        for j in range(1, sum+1):

            if arr[i-1] > j:
                t[i][j] = t[i-1][j]
            else:
                t[i][j] = t[i-1][j-arr[i-1]] or t[i-1][j]

    return t[n][sum]

arr = [3, 34, 4, 12, 5, 2]
sum = 10
n = len(arr)
t= [[False for j in range(sum+1)] for i in range(n+1)]

if subset(arr, sum, n) == True:
    print("found a subset")
else:
    print("no subset found")