import random
from os import path

import pygame as pg

from settings import *
from sprites.background import Background
from sprites.buffs import Buff
from sprites.enemy import Enemy
from sprites.player import Player


class Game:
    def __init__(self):
        pg.init()
        try:
            pg.mixer.init()
        except:
            print("Wyjebało Konfig")
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.font = pg.font.match_font(FONT_NAME)
        self.load_data()

    def new_game(self):
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.enemys = pg.sprite.Group()
        self.players = pg.sprite.Group()
        self.buffs= pg.sprite.Group()
        self.player = Player(self)
        self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.event()
            self.update()
            self.draw()

    def update(self):
        if random.randrange(1000) > 950:
            Enemy(self)
        if random.randrange(1001) > 990:
            Buff(self)
        self.all_sprites.update()

    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.background.image, self.background.rect)
        self.all_sprites.draw(self.screen)
        self.draw_text(f"Lives: {self.player.lives}", 36, WHITE, 50, 25)
        self.draw_text(f"Speed: {self.player.buffs['speed']}", 18, WHITE, 50, 45)
        self.draw_text(f"Size: {self.player.buffs['size']}", 18, WHITE, 50, 55)
        self.draw_text(f"Fragmentation: {self.player.buffs['fragmentation']}", 18, WHITE, 50, 65)
        self.draw_text(f"Piercing: {self.player.buffs['piercing']}", 18, WHITE, 50, 75)
        self.draw_text(f"Frequency: {self.player.buffs['frequency']}", 18, WHITE, 50, 85)
        pg.display.flip()

    def load_data(self):
        self.dir = path.dirname(__file__)
        self.img_dir = path.join(self.dir, "img")
        self.background = Background(path.join(self.img_dir, "bg.jpg"), [0, 0])
        self.background.image = pg.transform.scale(self.background.image, (WIDTH, HEIGHT))


    def show_start(self):
        pass

    def show_end(self):
        pass

    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)
