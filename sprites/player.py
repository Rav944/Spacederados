import pygame as pg
from os import path

from settings import *
from sprites.object import Object
from sprites.projectile import Projectile
from sprites.spritesheet import Spritesheet

vec = pg.math.Vector2


class Player(Object):
    def __init__(self, game):
        self._layer = PLATFORM_LAYER
        self.groups = game.all_sprites, game.players
        super().__init__(game, self.groups)
        self.projectiles = pg.sprite.Group()
        self.load_images()
        self.rect = self.image.get_rect()
        self.pos = (WIDTH / 2, HEIGHT - 200)
        self.rect.center = self.pos
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.shoot_timer = 0
        self.dash_timer = 0
        self.dashing = False
        self.dashing_vel = vec(0, 0)
        self.buffs = {"speed": 0, "size": 0, "fragmentation": 0, "piercing": 0, "frequency": 0}
        self.lives = 3

    def load_images(self):
        self.image = pg.image.load(path.join(self.game.img_dir, "S_01.png")).convert()
        self.image = pg.transform.scale(self.image, (50, 50))
        self.image = pg.transform.rotate(self.image, 180)
        self.image.set_colorkey(BLACK)

    def kill(self):
        self.lives -= 1
        if not self.lives:
            super().kill()
            self.game.playing = False

    def update(self):
        self.acc = vec(0, 0)
        now = pg.time.get_ticks()
        if now - self.dash_timer > 150 and self.dashing:
            self.dashing = False
            self.dashing_vel.x = 0
            self.dashing_vel.y = 0

        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.acc.x = -PLAYER_ACC - self.dashing_vel.x
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.acc.x = PLAYER_ACC + self.dashing_vel.x
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.acc.y = -PLAYER_ACC - self.dashing_vel.y
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.acc.y = PLAYER_ACC + self.dashing_vel.y
        if keys[pg.K_SPACE]:
            self.shoot()
        if keys[pg.K_LCTRL]:
            self.dash()

        self.acc.x += self.vel.x * PLAYER_FRICTION
        self.acc.y += self.vel.y * PLAYER_FRICTION
        self.vel += self.acc
        if abs(self.vel.x) < 0.3:
            self.vel.x = 0
        if abs(self.vel.y) < 0.3:
            self.vel.y = 0
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos

    def shoot(self):
        now = pg.time.get_ticks()
        if now - self.shoot_timer > 600 - self.buffs['frequency'] * 50:
            self.shoot_timer = now
            Projectile(self.game, self)

    def dash(self):
        now = pg.time.get_ticks()
        if now - self.dash_timer > 2000 and not self.dashing:
            self.dashing = True
            self.dash_timer = now
            self.dashing_vel.x = 3
            self.dashing_vel.y = 3
