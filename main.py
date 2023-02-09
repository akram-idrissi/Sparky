from game import engine


while engine.is_running():
    engine.process_input()
    engine.update()
    engine.draw()
