

def solve(items, capacity):
    memo={}
    def knapsack(n,w):
        key = str(n) + ',' + str(w)  # Join both arguments to make it easier with the memo
        if (key in memo):
            return memo[key]
        if n<1:
            return 0
        if w<items[n]:
            return knapsack(n-1,w)

    return knapsack(len(items)-1,capacity)