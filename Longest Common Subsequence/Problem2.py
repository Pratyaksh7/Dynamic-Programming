# 2. Longest Common Substring -> means continuous sequence

def longestSubstring(X,Y, n,m):
    # Initialization of first row and first column of the t matrix
    for i in range(n+1):
        for j in range(m+1):
            if i==0 or j==0:
                t[i][j] = 0

    for i in range(1, n+1):
        for j in range(1, m+1):
            if X[i-1] == Y[j-1]:    # comparing the 1st letter of both strings
                # t[i][j] = 1 + lcs(X,Y,n-1, m-1)
                t[i][j] = 1+t[i-1][j-1]

            else:
                t[i][j] = 0

    return t[n][m]

X = "abdefg"
Y = "abcefg"
n = len(X)
m = len(Y)
t= [[0 for j in range(m+1)] for i in range(n+1)]
print(longestSubstring(X,Y, n,m))