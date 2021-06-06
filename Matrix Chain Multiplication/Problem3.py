# 3. Evaluating expression to true / Boolean Parenthesization : Recursive
# We have to find the number of ways it can be true

def solve(string, i, j, isTrue):   # i/j -> True or False  k-> operator
    # base condition
    if i >j:
        return False
    if i==j:
        if isTrue == True:
            return string[i]== 'T'
        else:
            return string[i] == 'F'

    if t[i][j][isTrue] != -1:
        return t[i][j][isTrue]

    noOfWays = 0
    # k loop
    for k in range(i+1,j,2):
        leftTrue = solve(string, i, k-1, True)          # <--|
        leftFalse = solve(string, i, k-1, False)        #    |
        rightTrue = solve(string, k+1, j, True)         #    | -> temporary answers
        rightFalse = solve(string, k+1, j, False)       # <--|

        if string[k] == '&':
            if isTrue == True:
                noOfWays = noOfWays + (leftTrue * rightTrue)
            else:
                noOfWays = noOfWays + (leftFalse*rightTrue) + (leftTrue * rightFalse) + (leftFalse * rightFalse)

        elif string[k] == '|':
            if isTrue == True:
                noOfWays = noOfWays + (leftTrue * rightTrue) + (leftTrue * rightFalse) + (leftFalse * rightTrue)
            else:
                noOfWays = noOfWays + (leftFalse * rightFalse)

        elif string[k] == '^':
            if isTrue == True:
                noOfWays = noOfWays + (leftFalse * rightTrue) + (leftTrue * rightFalse)
            else:
                noOfWays = noOfWays + (leftTrue * rightTrue) + (leftFalse * rightFalse)

    t[i][j][isTrue] =  noOfWays
    return t[i][j][isTrue]

string = "T|T&F^T"
i = 0
j = len(string) - 1
isTrue = True

t = [[[-1 for _ in range(3)] for _ in range(len(string)+1)] for _ in range(len(string)+1)]
print(solve(string, i, j, isTrue))