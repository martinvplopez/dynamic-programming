# Given an amount and an infinite supply of coins S=[S1,S2,...Sm] get the number of possibles ways to change.

def coinChangeMemo(amount,supply):
    memo = {}
    def t(i,a):
        if a==0:
            return 1
        if a<0:
            return 0
        if i==len(supply):
            return 0
        if (i,a) in memo:
            return memo[(i,a)]
        memo[(i,a)]= t(i,a - supply[i])+ t(i+1,a)
        return memo[(i,a)]
    return t(0,amount)

print(coinChangeMemo(4,[1,2,3]))

