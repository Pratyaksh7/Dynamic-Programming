# 7. Min no of deletions from a string to make it a palindrome

def minDeletions(X,Y,n,m):
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                t[i][j] = 0

    for i in range(1, n+1):
        for j in range(1, m+1):
            if X[i-1] == Y[j-1]:
                # t[i][j] = 1 + lcs(X,Y, n-1,m-1)
                t[i][j] = 1 + t[i-1][j-1]

            else:
                t[i][j] = max(t[i-1][j], t[i][j-1])

    minDeltion = n - t[m][n] # if deletion is minimum then length of string is maximum
                            # so length of original string - longest palindromic subsequence = Min no of deletions
    return minDeltion

X= "agbcba"
m = len(X)

Y = "".join(reversed(X))
n = len(Y)
t = [[-1 for j in range(m+1)] for i in range(n+1)]

print(minDeletions(X,Y,n,m))