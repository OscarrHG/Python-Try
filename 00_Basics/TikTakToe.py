class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]  # Matriz 3x3 para el tablero
        self.current_player = 'X'  # Jugador actual

    def print_board(self):
        print("-------------")
        for row in self.board:
            print("| " + " | ".join(row) + " |")
            print("-------------")

    def make_move(self, row, col):
        if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            return True
        return False

    def check_win(self):
        # Verificar filas y columnas
        for i in range(3):
            if self.board[i][0] != ' ' and self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return True
            if self.board[0][i] != ' ' and self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return True
        # Verificar diagonales
        if self.board[0][0] != ' ' and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return True
        if self.board[0][2] != ' ' and self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return True
        return False

    def is_board_full(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def change_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play(self):
        while True:
            self.print_board()
            print(f"Turno del jugador {self.current_player}")
            try:
                row = int(input("Ingresa la fila (0, 1, 2): "))
                col = int(input("Ingresa la columna (0, 1, 2): "))
                if self.make_move(row, col):
                    if self.check_win():
                        self.print_board()
                        print(f"¡Jugador {self.current_player} gana!")
                        break
                    if self.is_board_full():
                        self.print_board()
                        print("¡Es un empate!")
                        break
                    self.change_player()
                else:
                    print("Movimiento inválido. Intenta de nuevo.")
            except ValueError:
                print("Entrada inválida. Por favor, ingresa números.")

if __name__ == "__main__":
    game = TicTacToe()
    game.play()