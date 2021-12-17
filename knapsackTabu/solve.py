# Recurrencia
# -----------
#  t(n,w) = 0                                    : if n <= 0 or w = 0
#         = t(n-1,w)                             : if w(n) > w
#         = max (t(n-1,w), t(n-1,w-w(n)) + B(n))

import numpy as np

def solve_tabulation(items, capacity):
    taken = []
    table = np.zeros((len(items)+1,capacity+1), dtype=int) # Tabla con tantas filas como elementos + 1 y tantas columnas como peso disponible + 1
    n=len(items)
    w=capacity

    def fill_table():
        for i in range(1,n+1):
            for j in range(0, w+1):
                if items[i-1].weight <= j:
                    if items[i-1].value + table[i-1,j-items[i-1].weight] > table[i-1,j]:
                        table[i,j]= items[i-1].value + table[i-1,j-items[i-1].weight]
                    else:
                        table[i,j]=table[i-1,j]
                else:
                    table[i,j]=table[i-1,j]
        return

    def fill_taken(n,w):
        i=n
        k=w
        while i>0 and k>0:
            if table[i,k] != table[i-1, k]: # Si es distinto a la fila anterior has cogido el elemento
                taken.insert(0,i)
                k=k-items[i-1].weight
                i=i-1
            else:
                i=i-1
        return
    fill_table()                # Relleno la tabla
    fill_taken(n,w)             # Genero la lista de items elegidos
    return table[n,w], taken
