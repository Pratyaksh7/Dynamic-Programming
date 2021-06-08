# 4. Scrambled string problem

def solve(string1, string2):
    if len(string1) != len(string2):
        return False
    n = len(string1)
    if not n:
        return True
    if string1 == string2:
        return True

    if t[n][n] != -1:
        return t[n][n]

    for i in range(1,n):
        condition1 = solve(string1[:i], string2[:i]) and solve(string1[i:], string2[i:])
        condition2 = solve(string1[:-i], string2[i:]) and solve(string1[-i:], string2[:i]) # doubt in logic

        if condition1 or condition2:
            t[n][n] =  True
            return t[n][n]

    t[n][n] = False
    return t[n][n]

string1 = "great"
string2 = "grate"
n = len(string1)

t = [[-1 for j in range(n+1)]for i in range(n+1)]

print(solve(string1, string2))