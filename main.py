import pygame as pg
from player import Player
from enemy import Enemy
from tile import Tile

# 1 for a tile
# 2 for a updown enemy
# 3 for a rightleft enemy

level0 = [
    [0, 1, 2, 0, 0, 3, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1],
    [0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1],
    [0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1],
    [0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1],
    [0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
]

class Game:
    def __init__(self):
        pg.init()
        self.win = pg.display.set_mode((1200, 800))
        self.clock = pg.time.Clock()
        self.FPS = 60
        self.player = Player()
        self.players = pg.sprite.Group()
        self.players.add(self.player)
        self.tiles = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.setup_tiles(level0)

    def draw(self):
        self.win.fill(pg.Color('white'))
        self.tiles.draw(self.win)
        self.players.draw(self.win)
        self.enemies.draw(self.win)
        self.tiles.update()
        self.players.update(self.tiles)
        self.enemies.update(self.tiles)

    def setup_tiles(self, level):
        for i in range(0, len(level)):
            for j in range(0, len(level[0])):
                if level[i][j] == 1:
                    self.tiles.add(Tile(j*100, i*100))
                elif level[i][j] == 2:
                    self.enemies.add(Enemy(j*100, i*100, 'updown'))
                elif level[i][j] == 3:
                    self.enemies.add(Enemy(j*100, i*100, 'leftright'))
    
    def run(self):
        while True:
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    pg.quit()

            self.draw()
            pg.display.update()
            self.clock.tick(self.FPS)

game = Game()
game.run()
