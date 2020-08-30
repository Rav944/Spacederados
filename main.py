# A place to mention the owners of art and sound
import pygame as pg

from game import Game

g = Game()
g.show_start()
while g.running:
    g.new_game()
    g.show_end()

pg.quit()

