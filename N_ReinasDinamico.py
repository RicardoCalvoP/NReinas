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
    for fila in tablero:
        print(' '.join(fila))


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
        """if size > 9:
            return"""
        print(f"Solución #{num_soluciones}")
        imprimir_tablero(tablero)
        return

    for columna in range(size):
        if es_seguro(tablero, fila, columna, size):
            tablero[fila][columna] = 'Q'
            colocar_reinas(tablero, fila + 1, size)
            tablero[fila][columna] = '*'


resolverNreinas(11)  # Cambia el número de reinas aquí
