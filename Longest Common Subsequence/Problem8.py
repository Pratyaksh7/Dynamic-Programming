# 8. Printing the shortest common supersequence

def Supersequence(X,Y,n,m):
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

    i = n
    j = m
    string = ""
    while(i > 0 or j > 0):
        if X[i-1] == Y[j-1]:
            string += X[i-1]
            i -= 1
            j-= 1

        else:
            if t[i-1][j] > t[i][j-1]:
                string += X[i-1]
                i-=1

            else:
                string += Y[j-1]
                j-=1

    while i>0:
        string += X[i-1]
        i -=1

    while j>0:
        string += Y[j-1]
        j -=1

    print(string[::-1])

X = "acbcf"
Y = "abcdaf"
# output: acbcdaf -> both x and y can be derived from output
n = len(X)
m = len(Y)

t = [[-1 for j in range(m+1)] for i in range(n+1)]

Supersequence(X,Y,n,m)