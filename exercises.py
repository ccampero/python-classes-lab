class Game:
    def __init__(self):
        self.turn = 'X'
        self.tire = False
        self.winner = None
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }

    def play_game(self):
        print("Welcome to Tic-Tac-Toe!")

    if __name__ == "__main__":
        game_instance = Game()
        game_instance.play_game()

    def print_board(self):
        b = self.board
        print(f"""
             A   B   C
        1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
        ----------
        2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
        ----------
        3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)
    
    def print_message(self):
        if self.tie:
            print("Tie game!")
        elif self.winner:
            print(f"{self.winner} wins the game!")
        else:
            print(f"It's player {self.turn}'s turn!")

    def render(self):
        self.print_board()
        self.print_message()

    def get_move(self):
        while True:
            move = input(f"Enter a valid move(example; A1): ").lower()
            if move in self.board and self.board[move] is None:
                self.board[move] = self.turn
                break
            else:
                print("Invalid move. Please try again.")

    def check_for_winner(self):
        b = self.board
        winning_combinations = [
            ['a1', 'b1', 'c1'],  
        ['a2', 'b2', 'c2'],  
        ['a3', 'b3', 'c3'],  
        ['a1', 'a2', 'a3'],  
        ['b1', 'b2', 'b3'],  
        ['c1', 'c2', 'c3'],  
        ['a1', 'b2', 'c3'],  
        ['c1', 'b2', 'a3']
        ]
        for combination in winning_combinations:
            if b[combination[0]] and b[combination[0]] == b[combination[1]] == b[combination[2]]:
                self.winner = b[combination[0]]
                return True
        return False

