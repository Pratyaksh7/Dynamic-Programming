# Longest Common Subsequence : Recursive -> Memoized -> Top Down DP

def lcs(X, Y, n, m):
    if n== 0 or m== 0:
        return 0

    if t[n][m] != -1:
        return t[n][m]

    else:
        if X[n-1] == Y[m-1]:
            t[n][m] = (1+lcs(X, Y, n-1, m-1))
            return t[n][m]

        else:
            t[n][m] =  max(lcs(X, Y, n, m-1), lcs(X, Y, n-1, m))
            return t[n][m]

X = "abcdf"
Y = "abedlf"
# o/p: 4 -> abdf
n = len(X)
m = len(Y)
t = [[-1 for j in range(m+1)] for i in range(n+1)]
print(lcs(X, Y, n, m))