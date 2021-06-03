# 2. Palindrome Partitioning: to get minimum no of partitionings
from sys import maxsize
def isPalindrome(x):
    return x == x[::-1]

def solve(string, i, j):
    if i >= j:
        return 0

    if isPalindrome(string[i:j+1]):  # to check if its palindrome
        return 0

    mn = maxsize
    for k in range(i, j):
        temp_ans = (1+ solve(string,i,k) + solve(string, k+1, j))

        mn = min(temp_ans, mn)

    return mn

string = "snitin"
# output: 1 because "s" and "nitin" both are palindrome AND ONLY ONE PARTITION IS DONE
i = 0
n = len(string)
j = n -1

print(solve(string, i, j))