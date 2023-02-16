import csv, pygame

from .sprite import Sprite
from .animSprite import AnimSprite

def parse_file(filename):
    if not filename: return
    data = []
    with open(filename) as file:
        rows = csv.reader(file, delimiter=',')
        for row in rows:
            temp = []
            for column in row:
                temp.append(int(column))                        
            data.append(temp) if len(temp) > 0 else ''
    return data
    

class Layer(Sprite):
    def __init__(self, actor, filename, tileset, tilesize):
        super().__init__(actor)

        self.tiles = []
        self.tile_rects = []
        self.tileset = tileset
        self.tilesize = tilesize
        self.filename = filename

        self.load_img(self.tileset)
        self.data = parse_file(self.filename)
        self.load_tiles()

    def load_tiles(self):
        columns = self.rect.w // self.tilesize

        for y, row in enumerate(self.data):
            for x, column in enumerate(row):
                if column != -1:
                    src_x = (column % columns) * self.tilesize
                    src_y = (column // columns) * self.tilesize

                    dest_x = x * self.tilesize
                    dest_y = y * self.tilesize
                    self.tiles.append([dest_x, dest_y, src_x, src_y])

    def update(self):
        pass
    

    def draw(self):
        self.tile_rects = []
        for tile in self.tiles:
            rect = pygame.Rect(tile[0] - self.offset[0], tile[1] - self.offset[1], self.tilesize, self.tilesize)
            self.tile_rects.append(rect) 
            self.screen.blit(self.image, (rect.x, rect.y), (tile[2], tile[3], self.tilesize, self.tilesize))


class SingleImgLayer(Layer):
    def __init__(self, actor, filename, tileset, tilesize):
        super().__init__(actor, filename, tileset, tilesize)
        self.data = self.load_tiles()

    def load_tiles(self):
        for y, row in enumerate(self.data):
            for x, column in enumerate(row):
                if column != -1:
                    dest_x = x * self.tilesize
                    dest_y = y * self.tilesize
                    self.tiles.append([dest_x, dest_y])

    def draw(self):
        for tile in self.tiles:
            self.screen.blit(self.image, (tile[0] - self.offset[0], tile[1] - self.offset[1]))


class AnimatedLayer(AnimSprite):
    def __init__(self, actor, filename, frames, tilesize):
        super().__init__(actor)
        
        self.tiles = []
        self.tile_rects = []
        self.tilesize = tilesize

        self.data = parse_file(filename)
        self.populate_animation(frames)
        self.load_tiles()

    def populate_animation(self, animations):
        self.animations = animations
        for k, frames in self.animations.items():
            temp = []
            for frame in frames:
                temp.append(self.load_img(frame))
            self.animations[k] = temp

    def load_tiles(self):
        for y, row in enumerate(self.data):
            for x, column in enumerate(row):
                if column != -1:
                    self.tiles.append([column, x * self.tilesize, y * self.tilesize])

    def draw(self):
        self.tile_rects = []
        for tile in self.tiles:
            self.current_animation = tile[0]
            self.image = self.animations[self.current_animation][int(self.index % len(self.animations[self.current_animation]))]
            
            rect = pygame.Rect(tile[1] - self.offset[0], tile[2] - self.offset[1], self.tilesize, self.tilesize)
            self.tile_rects.append(rect) 
            
            self.screen.blit(self.image, (rect.x, rect.y))
