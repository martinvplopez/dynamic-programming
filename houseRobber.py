# House Robber Problem
# items will be a list representing the profit of robbing every house
# houses which are next to each other can´t be robbed


# Memoized implementation
def houseRobberMemo(houses):
    memo={}
    def t(n):
        if n in memo:
            return memo[n]
        if n<=0:
            return 0
        memo[n]=max(t(n-2)+houses[n],t(n-1))
        return memo[n]
    return t(len(houses)-1)

print(houseRobberMemo([3,10,3,1,2]))


# Tabulation Implementation
