from game import Game

game = Game()

while game.is_running():
    game.process_input()
    game.update()
    game.draw()
