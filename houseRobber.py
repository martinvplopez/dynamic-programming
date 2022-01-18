# House Robber Problem
# items will be a list representing the profit of robbing every house
# houses which are next to each other can´t be robbed

# Memoized implementation
def houseRobberMemo(houses):
    memo={}
    def t(n):
        if n<=0:
            return 0
        if n in memo:
            return memo[n]
        memo[n]= max(t(n-2)+houses[n], t(n-1))
        return memo[n]
    return t(len(houses)-1)

# print(houseRobberMemo([3,10,3,1,2]))
# print(houseRobberMemo([3,10,3,1,2,14]))

# Tabulation Implementation
def houseRobberTabu(houses):
    # Filling the table process
    n=len(houses)
    table=[0]*(n)
    table[0]=houses[0]
    table[1]=max(houses[1],houses[0])
    for i in range(2,n):
        table[i] = max(table[i-2]+houses[i],table[i-1])
    # Get taken elements process
    taken=[]
    i=n-1
    b=table[len(table)-1]
    while i>0 and b>0:
        if table[i]<=b and table[i-1]!=table[i]:
            b=b-houses[i]
            taken.append(i+1)
        i-=1

    return table[n-1], taken




print(houseRobberTabu([3,10,3,1,2]))
print(houseRobberTabu([3,10,3,1,2,14]))