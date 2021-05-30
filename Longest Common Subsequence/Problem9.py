# 9. Longest Repeating subsequence

def repeatingSequence(X,Y,n,m):
    for i in range(n+1):
        for j in range(m+1):
            if i==0 or j==0:
                t[i][j] = 0;

    for i in range(1, n+1):
        for j in range(1, m+1):
            if X[i-1]== Y[j-1] and i != j :
                t[i][j] = 1 + t[i-1][j-1]

            else:
                t[i][j] = max(t[i-1][j], t[i][j-1])

    return t[n][m]

X = "aabebcdd"
n = len(X)
# output -> 3 because string of length 3 (abd) will be repeating twice in "aabebcdd"
Y = X
m = len(Y)

t = [[-1 for j in range(m+1)] for i in range(n+1)]
print(repeatingSequence(X,Y,n,m))