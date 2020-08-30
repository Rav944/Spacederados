import pygame as pg


class Object(pg.sprite.Sprite):
    def __init__(self, game, groups):
        pg.sprite.Sprite.__init__(self, groups)
        self.game = game
