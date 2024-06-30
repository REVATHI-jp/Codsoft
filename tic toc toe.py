import random

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # Represents the 3x3 board as a list
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # Display the board with numbers to show positions
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        # Returns a list of indices where the cell is empty
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        # Checks if there are any empty spots left
        return ' ' in self.board

    def num_empty_squares(self):
        # Counts the number of empty spots left
        return self.board.count(' ')

    def make_move(self, square, letter):
        # Place the letter (either 'X' or 'O') on the board at position square (0-8)
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Check if the latest move was a winning move
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True

        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False

def play_game():
    game = TicTacToe()

    print("Welcome to Tic Tac Toe!")
    game.print_board_nums()  # Show numbers to indicate positions

    letter = 'X'  # Human player starts with 'X'
    while game.empty_squares():
        if letter == 'O':
            # AI's turn
            square = random.choice(game.available_moves())
            game.make_move(square, letter)

            if game.current_winner:
                game.print_board()
                print(f"Sorry, {letter} wins!")
                break

            letter = 'X'
        else:
            # Human's turn
            game.print_board()
            square = None
            while square not in range(9) or not game.make_move(square, letter):
                try:
                    square = int(input(f"Player {letter}, choose a position (0-8): "))
                except ValueError:
                    print("Invalid input. Please enter a number between 0 and 8.")
                    continue

            if game.current_winner:
                game.print_board()
                print(f"Congratulations! Player {letter} wins!")
                break

            letter = 'O'

    if not game.current_winner:
        print("It's a tie!")

if __name__ == '__main__':
    play_game()
