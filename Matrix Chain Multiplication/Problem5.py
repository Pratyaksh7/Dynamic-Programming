# 5. Egg Dropping problem
# to find minimum no of attempts in worst case to get the threshold floor from where egg will not break
from sys import maxsize
def solve(e,f):
    if e==0:
        return f
    if f==0 or f==1:
        return f

    if t[e][f] != -1:
        return t[e][f]

    mn = maxsize
    for k in range(1,f):
        temp = 1 + max(solve(e-1,k-1), solve(e, f-k)) # max is used for the worst case
        mn = min(mn, temp) # min used for the minimum attempts

    t[e][f] = mn
    return t[e][f]

e= 3 # no of eggs
f= 5 # no of floors

t = [[-1 for j in range(f+1)]for i in range(e+1)]
print(solve(e,f))