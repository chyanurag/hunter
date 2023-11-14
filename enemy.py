import pygame as pg

class Enemy(pg.sprite.Sprite):
    def __init__(self, x, y, etype):
        super().__init__()
        self.image = pg.Surface([50, 50])
        self.image.fill('red')
        self.rect = self.image.get_rect()
        self.rect.x = x + self.rect.width / 2
        self.rect.y = y + self.rect.height / 2
        self.type = etype
        if self.type == 'updown':
            self.dir = 'down'
        else:
            self.dir = 'left'

    def update(self, tiles):
        if self.type == 'updown':
            if self.dir == 'up':
                for enemy in tiles.sprites():
                    if enemy.rect.colliderect(pg.Rect(self.rect.x, self.rect.y - 5, self.rect.width, self.rect.height)) or self.rect.y < 5:
                        self.dir = 'down'
                        return
                self.rect.y -= 5
            if self.dir == 'down':
                for enemy in tiles.sprites():
                    if enemy.rect.colliderect(pg.Rect(self.rect.x, self.rect.y + 5, self.rect.width, self.rect.height)) or self.rect.y > 750:
                        self.dir = 'up'
                        return
                self.rect.y += 5
        elif self.type == 'leftright':
            if self.dir == 'left':
                for enemy in tiles.sprites():
                    if enemy.rect.colliderect(pg.Rect(self.rect.x - 5, self.rect.y, self.rect.width, self.rect.height)) or self.rect.x < 5:
                        self.dir = 'right'
                        return
                self.rect.x -= 5
            if self.dir == 'right':
                for enemy in tiles.sprites():
                    if enemy.rect.colliderect(pg.Rect(self.rect.x + 5, self.rect.y, self.rect.width, self.rect.height)) or self.rect.x > 1195:
                        self.dir = 'left'
                        return
                self.rect.x += 5
