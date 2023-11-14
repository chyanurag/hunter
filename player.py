import pygame as pg
from bullet import Bullet

class Player(pg.sprite.Sprite):
    def __init__(self, ticks):
        super().__init__()
        self.image = pg.Surface([50, 50])
        self.image.fill(pg.Color('blue'))
        self.rect = self.image.get_rect()
        self.bullets = pg.sprite.Group()
        self.cooldown = 0
        self.dir = 'down'
        self.ticks = ticks

    def update(self, win, enemies, tiles):
        self.bullets.draw(win)
        self.bullets.update(tiles, enemies)
        key = pg.key.get_pressed()
        if key[pg.K_w]:
            for enemy in tiles.sprites():
                if enemy.rect.colliderect(pg.Rect(self.rect.x, self.rect.y - 5, self.rect.width, self.rect.height)) or self.rect.y < 5:
                    return
            self.rect.y -= 5
            self.dir = 'up'
        if key[pg.K_s]:
            for enemy in tiles.sprites():
                if enemy.rect.colliderect(pg.Rect(self.rect.x, self.rect.y + 5, self.rect.width, self.rect.height)) or self.rect.y+self.rect.height > 795:
                    return
            self.rect.y += 5
            self.dir = 'down'
        elif key[pg.K_a]:
            for enemy in tiles.sprites():
                if enemy.rect.colliderect(pg.Rect(self.rect.x - 5, self.rect.y, self.rect.width, self.rect.height)) or self.rect.x < 5:
                    return
            self.rect.x -= 5
            self.dir = 'left'
        elif key[pg.K_d]:
            for enemy in tiles.sprites():
                if enemy.rect.colliderect(pg.Rect(self.rect.x + 5, self.rect.y, self.rect.width, self.rect.height)) or self.rect.x+self.rect.width > 1195:
                    return
            self.rect.x += 5
            self.dir = 'right'
    def fire(self, ticks, enemies):
        if ticks - self.ticks > 500:
            self.bullets.add(Bullet(self.rect.center[0], self.rect.center[1], self.dir))
            self.ticks = ticks

