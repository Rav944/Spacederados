import random
import pygame as pg
from os import path

from settings import *
from sprites.mixins import CollisionMixin
from sprites.object import Object
vec = pg.math.Vector2


class Enemy(Object):
    def __init__(self, game):
        self._layer = ENEMY_LAYER
        self.groups = game.all_sprites, game.enemys
        super().__init__(game, self.groups)
        self.load_image()
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(50, WIDTH - 49)
        self.vel = vec(random.randrange(1, 10), random.randrange(1, 10))
        self.angle = 0
        self.dashing = False
        self.buffs = {}

    def load_image(self):
        image = random.choice(["meteor_01.png", "meteor_02.png"])
        x = random.randrange(25, 50)
        self.image = pg.image.load(path.join(self.game.img_dir, image)).convert()
        self.image = pg.transform.scale(self.image, (x, x))
        self.image.set_colorkey(BLACK)

    def update(self):
        # self.image = pg.transform.rotate(self.image, self.angle)
        # self.angle += 1 % 360
        if self.rect.x >= WIDTH or self.rect.x <= 0:
            self.vel.x *= -1
        self.rect.x += self.vel.x
        self.rect.y += self.vel.y
        self.collision()
        if self.rect.y > HEIGHT + 50:
            self.kill()

    def collision(self):
        hit = pg.sprite.spritecollide(self, self.game.players, False)
        if hit:
            if not hit[0].dashing:
                hit[0].kill()
                self.kill()
