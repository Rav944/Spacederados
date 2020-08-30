TITLE = "Spacederados"
WIDTH = 1500
HEIGHT = 1000
FPS = 60
FONT_NAME = "freesansbold.ttf"
HS_FILE = "highyscore.txt"
SPRITESHEET = "spritesheet_jumper.png"

PLAYER_ACC = 0.8
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8
PLAYER_JUMP = 20

ENEMY_FREQ = 5000
PLAYER_LAYER = 2
ENEMY_LAYER = 2
PLATFORM_LAYER = 1
PROJECTILE_LAYER = 0
BUFF_LAYER = 1
CLOUD_LAYER = 0

BUFFS = ["speed", "size", "fragmentation", "piercing", "frequency"]

BOOST_POWER = 40
POW_SPAWN_PCT = 10

PLATFORM_LIST = [(0, HEIGHT - 60),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4),
                 (125, HEIGHT - 350),
                 (350, 200),
                 (175, 100)]

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 155, 155)
BGCOOLOR = LIGHTBLUE
