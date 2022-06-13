def factMemo(n, memo={}):
    if n in memo:
        return memo[n]
    if n<=1:
        return 1
    memo[n]= n*factMemo(n-1)
    return memo[n]

def factTabu(n):
    table=[]
    table.append(1)
    table.append(1)
    for i in range(2,n+1):
        table.append(i*table[i-1])
    return table[n]

print(factMemo(10))
print(factTabu(10))