# Definir el tablero
tablero = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

# Función para dibujar el tablero
def dibujar_tablero():
    print(tablero[0] + " | " + tablero[1] + " | " + tablero[2])
    print("--+---+--")
    print(tablero[3] + " | " + tablero[4] + " | " + tablero[5])
    print("--+---+--")
    print(tablero[6] + " | " + tablero[7] + " | " + tablero[8])

# Función para comprobar si alguien ha ganado
def comprobar_ganador(simbolo):
    if tablero[0] == simbolo and tablero[1] == simbolo and tablero[2] == simbolo:
        return True
    elif tablero[3] == simbolo and tablero[4] == simbolo and tablero[5] == simbolo:
        return True
    elif tablero[6] == simbolo and tablero[7] == simbolo and tablero[8] == simbolo:
        return True
    elif tablero[0] == simbolo and tablero[3] == simbolo and tablero[6] == simbolo:
        return True
    elif tablero[1] == simbolo and tablero[4] == simbolo and tablero[7] == simbolo:
        return True
    elif tablero[2] == simbolo and tablero[5] == simbolo and tablero[8] == simbolo:
        return True
    elif tablero[0] == simbolo and tablero[4] == simbolo and tablero[8] == simbolo:
        return True
    elif tablero[2] == simbolo and tablero[4] == simbolo and tablero[6] == simbolo:
        return True
    else:
        return False

# Función para jugar
def jugar():
    jugador_actual = "X"
    juego_terminado = False

    while not juego_terminado:
        dibujar_tablero()
        print("Es el turno del jugador " + jugador_actual)

        # Pedir al jugador que elija una posición
        posicion = int(input("Elige una posición del 1 al 9: ")) - 1

        # Comprobar si la posición está disponible
        if tablero[posicion] == " ":
            tablero[posicion] = jugador_actual

            # Comprobar si el jugador ha ganado
            if comprobar_ganador(jugador_actual):
                dibujar_tablero()
                print("¡El jugador " + jugador_actual + " ha ganado!")
                juego_terminado = True
            # Comprobar si hay empate
            elif " " not in tablero:
                dibujar_tablero()
                print("¡Empate!")
                juego_terminado = True
            # Cambiar al siguiente jugador
            else:
                if jugador_actual == "X":
                    jugador_actual = "O"
                else:
                    jugador_actual = "X"
        else:
            print("Esa posición ya está ocupada. Elige otra.")

# Jugar al juego
jugar()
