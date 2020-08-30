import random
from os import path
import pygame as pg

from settings import *
from sprites.object import Object


class Buff(Object):
    def __init__(self, game):
        self._layer = BUFF_LAYER
        self.groups = game.all_sprites, game.buffs
        super().__init__(game, self.groups)
        self.load_images()
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(50, WIDTH - 49)
        self.type = random.choice(BUFFS)
        self.angle = 0

    def load_images(self):
        self.image = pg.image.load(path.join(self.game.img_dir, "buff_01.png")).convert()
        self.image = pg.transform.scale(self.image, (50, 50))
        self.image.set_colorkey(BLACK)

    def update(self):
        self.image = pg.transform.rotate(self.image, self.angle)
        self.angle += 1 % 360
        self.rect.y += 7
        if self.rect.y > HEIGHT + 50:
            self.kill()
        hit = pg.sprite.spritecollide(self, self.game.players, False)
        if hit:
            hit[0].buffs[self.type] += 1
            self.kill()
