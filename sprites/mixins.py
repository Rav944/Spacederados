import pygame as pg

from settings import *


class CollisionMixin:
    def check(self, colliders):
        hit = pg.sprite.spritecollide(self, colliders, False)
        if hit:
            if not hit[0].dashing:
                hit[0].kill()
                self.kill()

