# Recurrencia
# -----------
#  t(n,w) = 0                                    : if n <= 0 or w = 0
#         = t(n-1,w)                             : if w(n) > w
#         = max (t(n-1,w), t(n-1,w-w(n)) + B(n))

def solve_memoization(items, capacity):
    memo = {}
    taken = [0] * len(items)
    taken2=[]
    n=len(items)-1
    max_value=0

    # Utilizaremos esta función para generar la clave de acceso al
    # diccionario que utilizamos para guardar los resultados (mem).

    # Recordatorio de la documentación de Python 3:
    #    "Keys can be any immutable type; strings and numbers can
    #     always be keys. Tuples can be used as keys if they contain
    #     only strings, numbers, or tuples"

    def getKey(n,w): # Join both arguments to make it easier with the memo
        return str(n) + ' ' + str(w)

    def t(n,w):
        key=getKey(n,w)
        if n < 0:
            return 0
        if (key in memo):
            return memo[key]
        if w < items[n].weight:
            memo[key]= t(n - 1, w)
            return memo[key]
        memo[key]= max(t(n-1,w), t(n-1,w-items[n].weight)+items[n].value)
        return memo[key]

    max_value = t(n, capacity)  # Calculo el valor maximo


    # Fase2
    # De esta segunda fase se obtiene el parámetro taken del resultado comprobando la memoria

    # print(taken)
    # fill_taken(n,capacity)      # Genero la lista de items elegidos
    def fill_taken(n, w):
        v = max_value;
        while n >= 0 and w > 0:
            if n != 0:
                x = getKey(n, w)
                y = getKey(n - 1, w)
                if memo[x] != memo[y]:
                    taken[n] = 1
                    taken2.insert(0,n+1)
                    w -= items[n].weight
                    v -= items[n].value
            else:
                z = getKey(n, capacity)
                if memo[z] >= v and items[n].weight <= capacity:
                    taken[n] = 1
                    # taken2.insert(0,n+1)
            n -= 1;
        return

    fill_taken(n,capacity)
    print(taken2)
    return max_value, taken2
