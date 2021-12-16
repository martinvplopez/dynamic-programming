# Recurrencia
# -----------
#  t(n,w) = 0                                    : if n <= 0 or w = 0
#         = t(n-1,w)                             : if w(n) > w
#         = max (t(n-1,w), t(n-1,w-w(n)) + B(n))

def solve_memoization(items, capacity):
    memo = {}
    taken = []

    # Utilizaremos esta función para generar la clave de acceso al
    # diccionario que utilizamos para guardar los resultados (mem).

    # Recordatorio de la documentación de Python 3:
    #    "Keys can be any immutable type; strings and numbers can
    #     always be keys. Tuples can be used as keys if they contain
    #     only strings, numbers, or tuples"

    def t(n,w):
        key = str(n) + ',' + str(w)  # Join both arguments to make it easier with the memo
        if (key in memo):
            return memo[key]
        if n < 1:
            return 0
        if w < items[n].weight:
            memo[n]= t(n - 1, w)
            return memo[n]
        memo[n]= max(t(n-1,w), t(n-1,w-items[n].weight)+items[n].value)
        return memo[n]

    def fill_taken(n,w):
        # ...

        return

    n=len(items)-1

    max_value = t(n,capacity)   # Calculo el valor maximo
    print("Beneficio maximo:", max_value)
    fill_taken(n,capacity)      # Genero la lista de items elegidos

    return max_value, taken
