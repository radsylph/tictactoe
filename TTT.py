import random

board = [[' ' for i in range(3)] for j in range(3)]
jugador1 = 'X'
jugador2 = 'O'

def reset():
    global board
    board = [[' ' for i in range(3)] for j in range(3)]

def tablero():
    print()
    print(f' {board[0][0]} | {board[0][1]} | {board[0][2]} ')
    print('---|---|---')
    print(f' {board[1][0]} | {board[1][1]} | {board[1][2]} ')
    print('---|---|---')
    print(f' {board[2][0]} | {board[2][1]} | {board[2][2]} ')
    print()

def espacio():
    return sum([1 for i in range(3) for j in range(3) if board[i][j] == ' '])

def jugador():
    while True:

        x = int(input('\nJugador 1 elija una fila #(1-3): '))-1
        y = int(input('\nJugador 1 elija una columna #(1-3): '))-1

        if board[x][y] != ' ':
            print('Movimiento invalido')
        else:
            board[x][y] = jugador1
            break

def pc():
    while True:
        x = random.randint(0, 2)
        y = random.randint(0, 2)

        if board[x][y] != ' ':
            continue
        else:
            board[x][y] = jugador2
            break

def ganador():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != ' ':
            return board[i][0]
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != ' ':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]
    return ' '

def mensajeganador(winner):
    if winner == jugador1:
        print('HA GANADO EL JUGADOR 1')
    elif winner == jugador2:
        print('HA GANADO EL JUGADOR 2')
    else:
        print('EMPATE')

def main():
    respuesta = 1
    while respuesta == 1:
        winner = ' '
        reset()

        while winner == ' ' and espacio() != 0:
            tablero()
            jugador()
            winner = ganador()
            if winner != ' ' or espacio() == 0:
                break
            tablero()
            pc()
            winner = ganador()
            if winner != ' ' or espacio() == 0:
                break

        tablero()
        mensajeganador(winner)

        respuesta = int(input('\nTe gustaría jugar otra vez? (si = 1 / no = 0): '))

    print('Gracias por jugar')

if __name__ == '__main__':
    main()

