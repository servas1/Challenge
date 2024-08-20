def minesweeper(board):
    # Definimos las dimensiones del tablero
    rows = len(board)
    cols = len(board[0])

    # Función auxiliar para verificar si una celda está dentro del tablero
    def in_bounds(r, c):    
        if r >= 0 and r < rows:
            if c >= 0 and c < cols:
                return True
        return False
    
    def create_output_board(rows, cols):
        
        for r in range(rows):
            row = []
            for c in range(cols):
                row.append(0)
            output_board.append(row)

        return output_board

    # Movimientos posibles para las celdas vecinas (arriba, abajo, izquierda, derecha, y diagonales)
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    # Se crea el Tablero de salida

    output_board = []
    output_board = create_output_board(rows,cols)
    

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 1:
                # Si es una mina, colocamos un 9 en la celda correspondiente del tablero de salida
                output_board[r][c] = 9
            else:
                # Contamos las minas en las celdas vecinas
                mines_count = 0
                for direction in directions:
                    dr = direction[0]
                    dc = direction[1]
                    nr = r + dr
                    nc = c + dc
                    # Verificamos si la nueva celda está dentro de los límites del tablero
                    if in_bounds(nr, nc):
                        # Verificamos si la celda vecina tiene una mina
                        if board[nr][nc] == 1:
                            mines_count += 1
                # Asignamos el número de minas adyacentes
                output_board[r][c] = mines_count

    return output_board

input_board = [
    [0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0]
]

output_board = minesweeper(input_board)
for row in output_board:
    print(row)