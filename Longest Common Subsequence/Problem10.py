# 10. Sequence Pattern Matching: is sequence A is present in B

def sequenceMatch(X, Y, n,m):
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                t[i][j] = 0

    for i in range(1, n+1):
        for j in range(1, m+1):
            if X[i-1] == Y[j-1]:
                t[i][j] = 1 + t[i-1][j-1]

            else:
                t[i][j] = max(t[i][j-1], t[i-1][j])

    if t[n][m] == n:  # lcs == length of string X(smaller string)
        return True
    else:
        return False

X = "axy"
Y = "abxcpy"
# is sequence of X present in Y? here output is True because axy is present in abxcpy
n = len(X)
m = len(Y)

t = [[-1 for j in range(m+1)] for i in range(n+1)]

print(sequenceMatch(X, Y, n,m))