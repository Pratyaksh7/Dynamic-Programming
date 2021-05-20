# 4. Coin Change Problem 2 -> Minimum no of coins
import sys

def minCoins(coins, sum, n):
    for i in range(n+1):
        t[i][0] = 0

    for j in range(sum+1):
        t[0][j] = sys.maxsize

    for j in range(1, sum+1):
        if(j % coins[0] == 0):
            t[1][j] = j/coins[0]

        else:
            t[1][j] = sys.maxsize

    for i in range(2, n+1):
        for j in range(1,sum+1):
            if coins[i-1] > j:
                t[i][j] = t[i-1][j]

            else:
                t[i][j] = min(t[i][j - coins[i - 1]] + 1, t[i - 1][j])

    return t[n][sum]

coins = [1,2,3]
sum = 5
n = len(coins)

t = [[0 for j in range(sum+1)] for i in range(n+1)]
print(int(minCoins(coins, sum, n)))
