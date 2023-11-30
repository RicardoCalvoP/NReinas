import os

def resolverNreinas(size):
    global num_soluciones
    num_soluciones = 0
    tablero = crear_tablero(size)
    colocar_reinas(tablero, 0, size)
    print(f"Se encontraron {num_soluciones} soluciones para {size} reinas.")


def crear_tablero(size):
    tablero = [['*' for _ in range(size)] for _ in range(size)]
    return tablero


def imprimir_tablero(tablero):
    # Etiquetas de las columnas
    print('   ', end='')
    for i in range(len(tablero)):
        print(f'{chr(65 + i)} ', end='')
    print()

    for i, fila in enumerate(tablero):
        # Etiqueta de la fila
        print(f'{i + 1:2} ', end='')

        for casilla in fila:
            print(f'{casilla} ', end='')
        print()


def es_seguro(tablero, fila, columna, size):
    # Verificar la columna
    for i in range(fila):
        if tablero[i][columna] == 'Q':
            return False

    # Verificar la diagonal superior izquierda
    i, j = fila, columna
    while i >= 0 and j >= 0:
        if tablero[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Verificar la diagonal superior derecha
    i, j = fila, columna
    while i >= 0 and j < size:
        if tablero[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True


def colocar_reinas(tablero, fila, size):
    global num_soluciones
    if fila == size:
        num_soluciones += 1
        print(f"Solución #{num_soluciones}")
        imprimir_tablero(tablero)
        return

    for columna in range(size):
        if es_seguro(tablero, fila, columna, size):
            tablero[fila][columna] = 'Q'
            colocar_reinas(tablero, fila + 1, size)
            tablero[fila][columna] = '*'


os.system("cls")
size =  int(input("Ingrese el numero de Reinas: "))
os.system("cls")
resolverNreinas(size)  # Cambia el número de reinas aquí
