# 2. Rod Cutting Problem

def rodCutting(arr, price, length, n):
    for i in range(1, n+1):
        for j in range(1, length+1):
            if arr[i-1] > j:
                # t[i][j] = rodCutting(arr, price, j, i-1)
                t[i][j] = t[i-1][j]

            else:
                t[i][j] = max(price[i-1] + rodCutting(arr, price, j - arr[i-1], i) , rodCutting(arr, price, j, i-1))

    return t[n][length]

price = [1, 5, 8, 9, 10, 17, 17, 20]
length = 8
arr = [i for i in range(1, length+1)]
n = len(arr)
t= [[0 for j in range(length +1)] for i in range(n+1)]

print(rodCutting(arr, price, length, n))
