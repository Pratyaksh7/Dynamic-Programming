# 5. Minimum Subset Sum difference

def subset(arr, totalSum, n):
    for j in range(totalSum + 1):
        t[0][j] = False

    for i in range(n + 1):
        t[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, totalSum + 1):
            if arr[i - 1] > j:
                t[i][j] = t[i-1][j]

            else:
                t[i][j] = t[i-1][j-arr[i-1]] or t[i-1][j]


    vec = [-1 for i in range(int(totalSum/2))]
    for j in range(1, int(totalSum/2)):
        if t[n-1][j] == True:
            vec[j] = j

        else:
            vec[j] = -1

    finalArray = []
    for i in vec:
        if i >= 0:
            finalArray.append(totalSum - (2*i))

    return min(finalArray)

arr = [1,2,7]
totalSum = sum(arr)
n = len(arr)

t = [[False for j in range(totalSum+1)] for i in range(n+1)]

print(subset(arr, totalSum, n))
# this is not fully accurate yet