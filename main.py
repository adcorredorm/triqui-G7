def bienvenida():
    print('Bienvenidos al mejor juego de triqui del mundo mundial')
    print('Preparados?')

#TODO: verificar si el tablero esta lleno
def existe_ganador(tablero:list) -> bool:
    for i in range(3):
        # Verificamos filas
        if tablero[i][0] != 0 and tablero[i][0] == tablero[i][1] == tablero[i][2]:
            return True
        
        # Verificamos columnas
        if tablero[0][i] != 0 and tablero[0][i] == tablero[1][i] == tablero[2][i]:
            return True

    # Diagonal principal
    if tablero[0][0] != 0 and tablero[0][0] == tablero[1][1] == tablero[2][2]:
        return True
    
    # Diagonal secundaria
    if tablero[0][2] != 0 and tablero[0][2] == tablero[1][1] == tablero[2][0]:
        return True

    return False

def imprimir_tablero(tablero:list):
    for fila in tablero:
        print(fila)

#TODO: comprobar que la fila y la columna estan entre 0 y 2
#TODO: comprobar que la casilla no esta ocupada
def jugar(jugador:str, tablero:list):
    imprimir_tablero(tablero)
    fila:int = int(input('inserte el numero de la fila en la que realizara su movimiento '))
    col:int = int(input('inserte el numero de la columna en la que realizara su movimiento '))

    tablero[fila][col] = jugador


def alternar_jugador(jugador_actual:str):
    if jugador_actual == "X":
        return 'O'
    elif jugador_actual == "O":
        return 'X'

def mensaje_final(tablero:list, jugador_actual:str) -> str:
    if existe_ganador(tablero):
      if jugador_actual == 'X':
        print('El jugador con O es el ganador')
      elif jugador_actual == 'O':
        print('El jugador con X es el ganador')
    else:
        print('Hubo un empate')

def main():
    bienvenida()
    jugador:str = 'X'
    tablero:list = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    while not existe_ganador(tablero):
        jugar(jugador, tablero)
        jugador = alternar_jugador(jugador)
    mensaje_final(tablero, jugador)

if __name__ == '__main__':
    main()
