# 11. Minimum no of insertions in a string to make it palindrome

def minInsertion(X, Y, n, m):
    for i in range(n+1):
        for j in range(m+1):
            if i==0 or j==0:
                t[i][j] = 0

    for i in range(1, n+1):
        for j in range(1, m+1):
            if X[i-1] == Y[j-1]:
                t[i][j] = 1 + t[i-1][j-1]

            else:
                t[i][j] = max(t[i][j-1], t[i-1][j])

    # Min no of insertion = min no of deletion
    minIns = n - t[n][m]
    return minIns

X = "aebcbda"
n = len(X)

Y = "".join(reversed(X))
m = len(Y)

t = [[-1 for j in range(m+1)] for i in range(n+1)]

print(minInsertion(X, Y, n, m))




