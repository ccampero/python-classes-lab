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
