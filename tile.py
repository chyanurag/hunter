import pygame as pg

class Tile(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.Surface([100, 100])
        self.image.fill('black')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
