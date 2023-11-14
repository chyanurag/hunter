import pygame as pg

class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.image = pg.Surface([5, 10])
        self.image.fill('yellow')
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction

    def update(self, tiles, enemies):
        for enemy in enemies.sprites():
            if enemy.rect.colliderect(self.rect):
                enemy.health -= 30
                print(enemy.health)
                print('hit')
                self.kill()
        for tile in tiles.sprites():
            if tile.rect.colliderect(self.rect) or self.rect.x < 0 or self.rect.x > 1200 or self.rect.y < 0 or self.rect.y > 800:
                self.kill()
        if self.direction == 'up':
            self.rect.y -= 50
        elif self.direction == 'down':
            self.rect.y += 50
        elif self.direction == 'right':
            self.rect.x += 50
        elif self.direction == 'left':
            self.rect.x -= 50
