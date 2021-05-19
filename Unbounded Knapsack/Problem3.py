# Coin Change Problem 1 -> Maximum No of ways

def maxWays(coins, sum, n):
    for j in range(sum+1):
        t[0][j] = 0

    for i in range(n+1):
        t[i][0] = 1

    for i in range(1, n+1):
        for j in range(1, sum+1):
            if coins[i-1] > j:
                t[i][j] = t[i-1][j]

            else:
                # t[i][j] = maxWays(coins, j - coins[i-1], i) + maxWays(coins, j, i-1)
                t[i][j] = t[i][j- coins[i-1]] + t[i-1][j]
                # t[i][j- coins[i-1]] -> if selected j(sum) - coins[i-1](first coin value)

    return t[n][sum]

coins = [1,2,3]
sum = 5
n = len(coins)

t = [[0 for j in range(sum+1)] for i in range(n+1)]
print(maxWays(coins, sum, n))