# Function returns the numbers of ways a traveler can get to the bottom right of a grid starting from the top left position.
# Only going down or to the right is allowed
# m: number of rows, n: number of columns

# Classical recursive way 
def gridTravClassic(m,n):
    if(m==1 and n==1): # Base case (traveler in the detination)
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


print(gridTravMemo(18,18)) # 2333606220