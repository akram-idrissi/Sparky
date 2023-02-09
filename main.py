from game import game


while game.is_running():
    game.process_input()
    game.update()
    game.draw()
