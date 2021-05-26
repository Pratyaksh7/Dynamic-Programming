# 5. Program to find Minimum number of Insertions and deletions to convert 1st string to 2nd string

def lcs(X, Y, n, m):
    for i in range(n+1):
        for j in range(m+1):
            if i==0 or j==0:
                t[i][j] = 0

    for i in range(1, n+1):
        for j in range(1, m+1):
            if X[i-1] == Y[j-1]:
                # t[i][j] = 1+ lcs(X,Y,i-1,j-1)
                t[i][j] = 1+ t[i-1][j-1]

            else:
                t[i][j] = max(t[i-1][j], t[i][j-1])

    return t[n][m]

X = "heap"
Y = "pea"
n = len(X)
m = len(Y)

t = [[-1 for j in range(m+1)] for i in range(n+1)]

result = lcs(X, Y, n, m)
insertions = m - result
deletions = n - result
print("Number of insertions are:", insertions)
print("Number of deletions are:", deletions)