import numpy as np

def solveMemo(m,n, memo={}):
    if m==0 or n==0:
        return 1
    if (m,n) in memo:
        return memo[(m,n)]
    memo[(m,n)]= solveMemo(m-1,n) + solveMemo(m-1,n-1) + solveMemo(m,n-1)
    return memo[(m,n)]

#print(solveMemo(2,2))

def solveTabu(m,n):
    table=np.zeros((m+1,n+1),dtype=int)
    for i in range(0,m+1):
        for j in range(0,n+1):
            if i==0 or j==0:
                table[i][j]=1
            else:
                table[i][j]=table[i-1][j]+table[i-1][j-1]+table[i][j-1]
    return table[m,n]

print(solveTabu(0,0))