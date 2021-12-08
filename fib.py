# Function returns the nth element of the Fibonacci sequence
# Classical recursive way
def fibClassic(n): 
    if(n<=2):
        return 1
    return fibClassic(n-1)+fibClassic(n-2)

# print(fibClassic(50)) Not possible with this solution


# Memoization implementation of Fibonacci
def fibMemo(n, memo={}):
    if n in memo:
        return memo[n]
    if n<=2:
        return 1
    memo[n]= fibMemo(n-1,memo)+fibMemo(n-2,memo)
    return memo[n]

print(fibMemo(11))
print(fibMemo(7))
print(fibMemo(50))


