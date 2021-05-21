# Longest Common Subsequence : Recursive -> Memoized -> Top Down DP

def lcs(X, Y, n, m):
    if n== 0 or m== 0:
        return 0

    else:
        if X[n-1] == Y[m-1]:
            return (1+lcs(X, Y, n-1, m-1))

        else:
            return max(lcs(X, Y, n, m-1), lcs(X, Y, n-1, m))

X = "abcdef"
Y = "abedlf"
# o/p: 4 -> abdf
n = len(X)
m = len(Y)

print(lcs(X, Y, n, m))