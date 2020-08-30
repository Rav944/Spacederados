from os import path
import pygame as pg


from settings import *
from sprites.mixins import CollisionMixin
from sprites.object import Object


class Projectile(Object):
    def __init__(self, game, shooter):
        self._layer = PROJECTILE_LAYER
        self.groups = game.all_sprites
        super().__init__(game, self.groups)
        self.shooter = shooter
        self.projectile_x = 5 + self.shooter.buffs.get("size")
        self.projectile_y = 20
        self.speed = 4 + self.shooter.buffs.get("speed", 0)
        self.load_images()
        self.rect = self.image.get_rect()
        self.rect.x = self.shooter.rect.centerx
        self.rect.y = self.shooter.rect.top
        self.piercing = self.shooter.buffs.get("piercing", 0)

    def load_images(self):
        self.image = pg.image.load(path.join(self.game.img_dir, "laser_01.png")).convert()
        self.image = pg.transform.scale(self.image, (self.projectile_x, self.projectile_y))
        self.image.set_colorkey(BLACK)

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()
        self.collision()

    def collision(self):
        hit = pg.sprite.spritecollide(self, self.game.enemys, False)
        if hit and not hit[0].dashing:
            hit[0].kill()
            if not self.piercing:
                self.kill()
            else:
                self.piercing -= 1
