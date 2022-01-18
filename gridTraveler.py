# Function returns the numbers of ways a traveler can get to the bottom right of a grid starting from the top left position.
# Only going down or to the right is allowed
# m: number of rows, n: number of columns
import numpy as np

# Classical recursive way 
def gridTravClassic(m,n): # m=rows, n=columns
    if(m==1 and n==1): # Base case (traveler in the destination)
        return 1
    if(m==0 or n==0): # Invalid grid
        return 0
    return gridTravClassic(m-1,n) + gridTravClassic(m,n-1) # Result will be the sum of going down and going right

""" print(gridTravClassic(3,3)) # 6
print(gridTravClassic(2,3)) # 3
print(gridTravClassic(18,18)) # Not possible with  this solution """


# Memoization implemented
def gridTravMemo(m,n, memo={}):
    key= str(m) + ',' + str(n) # Join both arguments to make it easier with the memo
    if(key in memo):
        return memo[key]
    if(m==1 and n==1): # Base case (traveler in the detination)
        return 1
    if(m==0 or n==0): # Invalid grid
        return 0
    memo[key]=gridTravMemo(m-1,n,memo) + gridTravMemo(m,n-1,memo)
    return memo[key]  # Result will be the sum of going down and going right

#
# print(gridTravMemo(2,2)) # 2
# print(gridTravMemo(18,18)) # 2333606220
print(gridTravMemo(5,5)) # 70


# Tabulation implementation
def gridTravTab(m,n):
    # Rellenar tabla
    table=np.zeros((m+1,n+1), dtype=int)
    for i in range(1,m+1):
        for j in range(1,n+1):
            if i!= 1 and j!=1:
                table[i][j]=table[i-1][j] + table[i][j-1]
            else:
                table[i][j]=1
    return table[m][n]

print(gridTravTab(5,5))