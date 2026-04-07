
# 1
def suma_impares_diagonal(matriz, i=0):
    n = len(matriz)
    if i >= n:
        return 0
    suma = 0
    if matriz[i][i] % 2 != 0:
        suma += matriz[i][i]
    if i != n - 1 - i:
        if matriz[i][n - 1 - i] % 2 != 0:
            suma += matriz[i][n - 1 - i]
    return suma + suma_impares_diagonal(matriz, i + 1)

m1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
m2 = [
    [2, 4, 6, 8],
    [1, 3, 5, 7],
    [9, 11, 13, 15],
    [10, 12, 14, 16]
]

print("\nPrimer punto:")
print("Escenario 1: ",suma_impares_diagonal(m1))
print("Escenario 2: ",suma_impares_diagonal(m2))

# 2
def suma_digitos(n):
    if n == 0:
        return 0
    return n % 10 + suma_digitos(n // 10)
def super_digito(n):
    if n < 10:
        return n
    return super_digito(suma_digitos(n))

print("\nSegundo punto:")
print("Escenario 1: ",super_digito(9875))
print("Escenario 2: ",super_digito(123456))

# 3
def juego(lista, inicio, fin, turno, p1=0, p2=0):
    if inicio > fin:
        return [p1, p2]
    if lista[inicio] > lista[fin]:
        elegido = lista[inicio]
        inicio += 1
    else:
        elegido = lista[fin]
        fin -= 1
    if turno == 1:
        return juego(lista, inicio, fin, 2, p1 + elegido, p2)
    else:
        return juego(lista, inicio, fin, 1, p1, p2 + elegido)

print("\nTercer punto:")
print("Escenario 1: ",juego([4, 1, 7, 3], 0, 3, 1))
print("Escenario 2: ",juego([10, 2, 8, 1, 9], 0, 4, 1))

# 4
def decodificar(cadena):
    if '[' not in cadena:
        return cadena
    i = cadena.find('[')
    k = int(cadena[:i])
    j = cadena.find(']')
    texto = cadena[i + 1:j]
    resultado = k * texto
    return resultado + decodificar(cadena[j + 1:])

print("\nCuarto punto:")
print("Escenario 1: ",decodificar("3[a]2[bc]"))
print("Escenario 2: ",decodificar("2[x]3[yz]\n"))