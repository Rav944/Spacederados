import pygame as pg


class Background(pg.sprite.Sprite):
    def __init__(self, image_file, location):
        super().__init__()
        self.image = pg.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
