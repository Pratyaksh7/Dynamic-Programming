# 4. Scrambled string problem

def solve(string1, string2):
    if len(string1) != len(string2):
        return False
    n = len(string1)
    if not n:
        return True
    if string1 == string2:
        return True

    for i in range(1,n):
        condition1 = solve(string1[:i], string2[:i]) and solve(string1[i:], string2[i:])
        condition2 = solve(string1[:-i], string2[i:]) and solve(string1[-i:], string2[:i]) # doubt in logic

        if condition1 or condition2:
            return True

    return False

string1 = "great"
string2 = "grate"

print(solve(string1, string2))