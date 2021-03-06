# Function returns boolean indicating whether or not it´s possible to get the targetSum from numbers array
# Numbers can be used more than once and all numbers are non-negative
# Classical recursive way
def canSumClassic(targetSum, numbers): 
    if(targetSum==0):
        return True
    if(targetSum<0):
        return False
    for num in numbers:
        if(canSumClassic(targetSum-num,numbers)== True):
            return True
    return False

# print(canSumClassic(18,[5,3,4,7])) #True
""" print(canSumClassic(600000,[7,14])) # Not possible """


# Memoization implementation of canSum
def canSumMemo(targetSum, numbers, memo={}): 
    if(targetSum in memo):
        return memo[targetSum]
    if(targetSum==0):
        return True
    if(targetSum<0):
        return False
    for num in numbers:
        if(canSumMemo(targetSum-num,numbers,memo)== True):
            memo[targetSum]=True
            return True
    memo[targetSum]=False
    return False


# print(canSumMemo(2000,[20]))



def canSumTab(targetSum, numbers):
    table=[False] * (targetSum+1)
    table[0]=True
    for i in range(0,len(table)-1):
        if table[i] is True:
            for num in numbers:
                if i+num < len(table):
                    table[i+num]=True
    return table[targetSum]

print(canSumTab(2000,[20])) # True
print(canSumTab(18,[5,3,4,7])) #True
print(canSumTab(600000,[7,14])) # False