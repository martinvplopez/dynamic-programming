# Function returns the nth element of the Fibonacci sequence
# Classical recursive way
def fibClassic(n): 
    if(n<=2):
        return 1
    return fibClassic(n-1)+fibClassic(n-2)

#print(fibClassic(50)) #Not possible with this solution


# Memoization implementation of Fibonacci
def fibMemo(n, memo={}):
    if n in memo:
        return memo[n]
    if n<=2:
        return 1
    memo[n]= fibMemo(n-1)+fibMemo(n-2)
    return memo[n]

# print(fibMemo(11))
# print(fibMemo(7))
# print(fibMemo(50))

# Tabulation implementation
def fibTab(n):
    table=[]
    table.append(0)
    table.append(1)
    for i in range(2, n+1):
        table.append(table[i-2]+table[i-1])
    return table[n]

# print(fibTab(6)) # 8
# print(fibMemo(7)) # 13
print(fibMemo(50)) # 12586269025





