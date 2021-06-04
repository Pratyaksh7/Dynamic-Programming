# 2. Palindrome Partitioning: to get minimum no of partitionings
from sys import maxsize
def isPalindrome(x):
    return x == x[::-1]

def solve(string, i, j):
    if i >= j:
        return 0

    if isPalindrome(string[i:j+1]):  # to check if its palindrome
        return 0

    if t[i][j] != -1:
        return t[i][j]

    mn = maxsize
    for k in range(i, j):
        if t[i][k] != -1:       # more optimised code from here
            left = t[i][k]
        else:
            left = solve(string,i,k)
            t[i][k] = left

        if t[k+1][j] != -1:
            right = t[k+1][j]
        else:
            right = solve(string, k+1, j)
            t[k+1][j] = right           # till here

        temp_ans = (1+ left + right)

        mn = min(temp_ans, mn)

    t[i][j] = mn
    return t[i][j]

string = "snitin"
# output: 1 because "s" and "nitin" both are palindrome AND ONLY ONE PARTITION IS DONE
i = 0
n = len(string)
j = n -1

t = [[-1 for _ in range(n+1)] for _ in range(n+1)]
print(solve(string, i, j))