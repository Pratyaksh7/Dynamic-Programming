# 3. Printing Longest Common subsequence

def printingLCS(X,Y,n,m):
    for i in range(n+1):
        for j in range(m+1):
            if i==0 or j==0:
                t[i][j] = 0

    for i in range(1,n+1):
        for j in range(1, m+1):
            if X[i-1] == Y[j-1]:
                t[i][j] = 1+ t[i-1][j-1]

            else:
                t[i][j] = max(t[i-1][j], t[i][j-1])

    string = ""
    i,j = n,m
    while (i>0 and j>0):            # starting the iterating from the bottom right of matrix t
        if X[i-1] == Y[j-1]:
            string += X[i-1]
            i -= 1
            j -= 1             # i-- and j-- bring it back diagonally

        else:
            if t[i-1][j] > t[i][j-1]:
                i -=1                   # i-- bring it upward
            else:
                j-=1                    # j-- bring it leftward

    return string[::-1] # reversing the string

X = "acbcf"
Y = "abcdaf"
n = len(X)
m = len(Y)

t = [[0 for j in range(m+1)] for i in range(n+1)]

print(printingLCS(X,Y,n,m))