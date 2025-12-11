from game.gamevar import GameVar
from game.gamehandler import GameHandler

if __name__ == '__main__':
    game_var = GameVar()
    game_handler = GameHandler()
    game_handler.run(game_var)
