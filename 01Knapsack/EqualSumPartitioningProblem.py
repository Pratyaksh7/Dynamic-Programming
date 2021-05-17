# 3. Equal Sum Partitioning problem

def subset(arr, sum, n):
    t= [[False for j in range(sum+1)] for i in range(n+1)]

    for j in range(sum+1):
        t[0][j] = False

    for i in range(n+1):
        t[i][0] = True

    for i in range(1, n+1):
        for j in range(1, sum+1):
            if arr[i-1] > j:
                t[i][j] = subset(arr, j, i-1)

            else:
                t[i][j]= subset(arr, j - arr[i-1], i-1) or subset(arr, j, i-1)

    return t[n][sum]

arr = [5,11,5, 3]
n = len(arr)
totalSum = sum(arr)

if totalSum % 2 != 0:
    print("False")
else:
    print(subset(arr,int(totalSum/2), n))