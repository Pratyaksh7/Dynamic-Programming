# 6. Longest Palindromic Subsequence
# inputs will be just one string

def lps(X,Y,n,m):
    for i in range(n+1):
        for j in range(m+1):
            if i== 0 or j == 0:
                t[i][j] = 0

    for i in range(1,n+1):
        for j in range(1, m+1):
            if X[i-1] == Y[j-1]:
                # t[i][j] = 1 + lps(X,Y,n-1,m-1)
                t[i][j] = 1 + t[i-1][j-1]

            else:
                # t[i][j] = max(lcs(X,Y,n,m-1), lcs(X,Y,n-1,m))
                t[i][j] = max(t[i][j-1], t[i-1][j])

    return t[n][m]

X = "agbcba"
n = len(X)

Y = "".join(reversed(X))
m = len(Y)

t = [[-1 for j in range(m+1)] for i in range(n+1)]

print(lps(X,Y,n,m))