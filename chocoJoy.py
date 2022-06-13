# You’ve just got a tube of chocolates and plan to eat one piece a day – either by picking the one on the left or the right.
# Each piece has a positive integer that indicates how tasty it is. Since taste is subjective, there is also an expectancy factor.
# A piece will taste better if you eat it later: if the taste is m (as in hmm) on the first day, it will be km on day number k.
# Your task is to design an efficient algorithm that computes an optimal chocolate eating strategy and tells you how much pleasure to expect.
# Problem from: https://yourbasic.org/algorithms/dynamic-programming-explained/

import numpy as np

def chocoJoyMemo(chocos, memo={}):
    def solve(chocos, day):
        if day==1:
            return day*chocos[0]
        left= day*solve(chocos[1:], day-1)
        right= day*solve(chocos[:-1], day-1)
        if (left,right) in memo:
            return memo[(left,right)]
        memo[(left,right)]=max(left,right)
        return memo[(left,right)]
    return solve(chocos, len(chocos))

def chocoJoyTabu(chocos): # Not done
    n=len(chocos)+1
    table=np.zeros((n,n), dtype=int)
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j!=1:
                table[i][j]=max(j*table[i][j-1], j*table[i][j-1])
            else:
                table[i][j]=j*chocos[0]

    return table[n][n]



print(chocoJoyMemo([1,2,3,4,7,4,5,6,7,5,8])) # 319334400
print(chocoJoyTabu([1,2,3,4,7,4,5,6,7,5,8])) #
