
def solveMemo(itemsB,itemsW,capacity,memo={}):
    def t(n,w):
        key=(n,w)
        if n<0: # Si no quedan elementos
            return 0
        if key in memo:
            return memo[key]
        if itemsW[n]>w: # Si el peso del elemento es mayor a la capacidad de la mochila
            memo[key]=t(n-1,w)
            return memo[key]
        memo[key]= max(t(n-1,w), t(n-1,w-itemsW[n])+itemsB[n]) # Caso general: máximo de coger y no coger un elemento
        return memo[key]
    return t(len(itemsB)-1,capacity)




print(solveMemo([3,4,5,6],[2,3,4,5],5))