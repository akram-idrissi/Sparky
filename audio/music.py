import pygame


class Music():
    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 2, 512)
        
    def load_sound(self, path):
        pygame.mixer.music.load(path) if path else ''

    def play(self, time):
        pygame.mixer.music.play(time)

    def pause(self):
        pygame.mixer.music.pause()

    def unpause(self):
        pygame.mixer.music.unpause()

    def stop(self):
        pygame.mixer.music.stop()

    def fade_out(self   , time):
        pygame.mixer.music.fade_out(time)

    def close(self):
        pygame.mixer.quit()

    # getters setters
    def set_volume(self, num):
       pygame.mixer.music.set_volume(num)
       