# 4. Shortest Common SuperSequence : Shortest combined string from which both the input strings sequence will be generated

def superSequence(X,Y, n,m):
    for i in range(n+1):
        for j in range(m+1):
            if i==0 or j==0:
                t[i][j] = 0

    for i in range(1, n+1):
        for j in range(1, m+1):
            if X[i-1] == Y[j-1]:
                t[i][j] = 1+ t[i-1][j-1]

            else:
                t[i][j] = max(t[i-1][j], t[i][j-1])

    return n+m-t[n][m]    # string1 + string2 - LCS


X = "aggtab"
Y = "gxtxayb"
n = len(X)
m = len(Y)

t = [[-1 for j in range(m+1)] for i in range(n+1)]

print(superSequence(X,Y, n,m))