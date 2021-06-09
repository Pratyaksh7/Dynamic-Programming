# 5. Egg Dropping problem
# to find minimum no of attempts in worst case to get the threshold floor from where egg will not break
from sys import maxsize
def solve(e,f):
    if e==0:
        return f
    if f==0 or f==1:
        return f
    mn = maxsize
    for k in range(1,f):
        temp = 1 + max(solve(e-1,k-1), solve(e, f-k)) # max is used for the worst case
        mn = min(mn, temp) # min used for the minimum attempts

    return mn

e= 3 # no of eggs
f= 5 # no of floors

print(solve(e,f))