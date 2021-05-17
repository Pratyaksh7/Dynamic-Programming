# 1. knapsack Problem (0-1)

def knapsack(wt, val, W, n):
    if n==0 or W==0:
        return 0

    if t[n][W] != 0:
        return t[n][W]

    else:
        if wt[n-1] > W:
            t[n][W]= knapsack(wt, val, W, n-1)
            return t[n][W]

        else:
            t[n][W]= max(val[n-1] + knapsack(wt, val, W - wt[n-1], n-1),  knapsack(wt, val, W, n-1))
            return t[n][W]

wt = [10, 20, 30]
val = [60, 100, 120]
W= 50
n=len(wt)
t = [[0 for j in range(W+1)] for i in range(n+1)]
print(knapsack(wt, val, W, n))