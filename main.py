from game import Game

game = Game()

while game.isRunning():
    game.processInput()
    game.update()
    game.draw()
