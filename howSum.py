# Function returns array of combinations from the input array to get the sum represented by targetSum 
# If no combination is possible--> return None
# Return any correct combination
# Numbers can be used more than once and all numbers are non-negative
# Classical recursive way
def howSumClassic(targetSum, numbers):
    if(targetSum==0):
        return []
    if(targetSum<0):
        return None
    for num in numbers:
        res= howSumClassic(targetSum-num,numbers)
        if( res != None):
            return res + [num]
    return None

print(howSumClassic(7,[5,3,4,7])) # 7 / 3,4
print(howSumClassic(8,[2,3,5])) # 2,2,2,2 / 3,5
print(howSumClassic(7,[2,4])) # None
#print(howSumClassic(300,[7,14])) # None (not possible with this method)

# Memoization implementation of howSum
def howSumMemo(targetSum, numbers, memo={}):
    if (targetSum in memo):
        return memo[targetSum]
    if(targetSum==0):
        return []
    if(targetSum<0):
        return None
    for num in numbers:
        res=howSumMemo(targetSum-num,numbers)
        if(res!=None):
            memo[targetSum]= res + [num]    
            return memo[targetSum]   
    memo[targetSum]=None
    return None

print(howSumMemo(7,[5,3,4,7])) # 7 / 3,4
print(howSumMemo(8,[2,3,5])) # 2,2,2,2 / 3,5
print(howSumMemo(7,[2,4])) # None 
print(howSumMemo(300,[7,14])) # None  


