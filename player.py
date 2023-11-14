import pygame as pg

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface([50, 50])
        self.image.fill(pg.Color('blue'))
        self.rect = self.image.get_rect()

    def update(self, enemies):
        key = pg.key.get_pressed()
        if key[pg.K_w]:
            for enemy in enemies.sprites():
                if enemy.rect.colliderect(pg.Rect(self.rect.x, self.rect.y - 5, self.rect.width, self.rect.height)) or self.rect.y < 5:
                    return
            self.rect.y -= 5
        if key[pg.K_s]:
            for enemy in enemies.sprites():
                if enemy.rect.colliderect(pg.Rect(self.rect.x, self.rect.y + 5, self.rect.width, self.rect.height)) or self.rect.y+self.rect.height > 795:
                    return
            self.rect.y += 5
        elif key[pg.K_a]:
            for enemy in enemies.sprites():
                if enemy.rect.colliderect(pg.Rect(self.rect.x - 5, self.rect.y, self.rect.width, self.rect.height)) or self.rect.x < 5:
                    return
            self.rect.x -= 5
        elif key[pg.K_d]:
            for enemy in enemies.sprites():
                if enemy.rect.colliderect(pg.Rect(self.rect.x + 5, self.rect.y, self.rect.width, self.rect.height)) or self.rect.x+self.rect.width > 1195:
                    return
            self.rect.x += 5


