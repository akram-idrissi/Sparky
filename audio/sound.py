import pygame
from random import choice


class Sound:
    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 2, 512)
        self.sounds = {}
        self.current_sound = None
        self.current_sound_on = None

    def load_sound(self, path):
        return pygame.mixer.Sound(path) if path else None

    def add_sound(self, name, sounds):
        if name and len(sounds) > 0:
            self.sounds[name] = [self.load_sound(sound) for sound in sounds]
            self.current_sound = name

    def append_to_sound(self, name, sounds):
        if name and len(sounds) > 0:
            self.sounds[name] += [self.load_sound(sound) for sound in sounds]

    def play(self):
        self.current_sound_on = choice(self.sounds[self.current_sound])
        self.current_sound_on.play()

    def stop(self):
        self.current_sound_on.stop()

    def fade_out(self, time):
        self.current_sound_on.fade_out(time)

    def close(self):
        pygame.mixer.quit()

    # getters setters
    def set_sound(self, name, sounds):
        if name in self.sounds.keys and len(sounds) > 0:
            self.sounds[name] = [self.load_sound(sound) for sound in sounds]

    def get_sounds(self, name):
        self.sounds[name] if name in self.sounds.keys else None

    def set_current_sound(self, name):
        self.current_sound = name

    def get_current_sound(self):
        return self.current_sound

    def set_num_channels(self, num):
        pygame.mixer.set_num_channels(num)

    def get_num_channels(self):
        pygame.mixer.get_num_channels()

    def set_volume(self, num):
        self.current_sound_on.set_volume(num)
