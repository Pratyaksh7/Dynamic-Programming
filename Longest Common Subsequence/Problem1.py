# Longest Common Subsequence : Recursive -> Memoized -> Top Down DP

def lcs(X, Y, n, m):
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                t[i][j] = 0

    for i in range(1, n+1):
        for j in range(1, m+1):
            if X[i-1] == Y[j-1]:
                t[i][j] = 1+t[i-1][j-1]

            else:
                t[i][j] = max(t[i][j-1], t[i-1][j])

    return t[n][m]

X = "abcdf"
Y = "abedlf"
# o/p: 4 -> abdf
n = len(X)
m = len(Y)
t = [[-1 for j in range(m+1)] for i in range(n+1)]
print(lcs(X, Y, n, m))