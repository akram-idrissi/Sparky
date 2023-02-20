import pygame

def right_collision(rect1, rect2):
    return rect1.right >= rect2.left


def left_collision(rect1, rect2):
    return rect1.left <= rect2.right


def top_collision(rect1, rect2):
    return rect1.top <= rect2.bottom


def bottom_collision(rect1, rect2):
    return rect1.bottom >= rect2.top


def collidedtiles(rect, tiles):
    return [tile for tile in tiles if tile.colliderect(rect)]


def horizontal_movement(rect, velocity, tiles):
    collisions = {'right': False, 'left': False}

    for tile in tiles:
        if velocity.x > 0:
            rect.right = tile.left
            collisions['right'] = True
        elif velocity.x < 0:
            rect.left = tile.right
            collisions['left'] = True
    
    return rect, collisions


def vertical_movement(rect, velocity, tiles):
    collisions = {'top': False, 'bottom': False}

    for tile in tiles:
        if velocity.y > 0:
            rect.bottom = tile.top
            collisions['bottom'] = True
        elif velocity.y < 0:
            rect.top = tile.bottom
            collisions['top'] = True
    
    return rect, collisions