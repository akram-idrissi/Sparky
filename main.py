from core.game import engine


while engine.running:
    engine.process_input()
    engine.update()
    engine.draw()
