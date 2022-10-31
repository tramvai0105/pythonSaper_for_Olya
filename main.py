import pygame
from pygame.locals import *
from random import randrange

ROWS = 16
COLS = 16
WIDTH = ROWS * 50
HEIGHT = COLS * 50
FPS = 30
BOMBS = 50
GAMESTAGE = "game"


pygame.init()
FONTSM = pygame.font.Font('fonts/font.otf', 60)
FONT = pygame.font.Font('fonts/font.otf', 200)
FONTW = pygame.font.Font('fonts/font.otf', 400)

restart_text = FONTSM.render('click left button to restart...', False, 'blue')
restart_rect = restart_text.get_rect(center=(WIDTH // 2, HEIGHT*7 // 10))

game_over_text = FONT.render('GAME OVER', False, 'red')
game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

game_win_text = FONTW.render('WIN', False, 'green')
game_win_rect = game_win_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Olya Saper SSS Rang")
clock = pygame.time.Clock()

tiles = pygame.sprite.Group()


class Tile(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, num=0, status="closed"):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/tile.jpg').convert_alpha()
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.num = num
        self.status = status
        self.rect.topleft = (self.x, self.y)

    def get_tile(self, direct):
        if direct == "left":
            if self.x != 0:
                filtredbyy = [t for t in tilesArr if t.y == self.y]
                filtredbyx = [t for t in filtredbyy if t.x == self.x - 50]
                return filtredbyx[0]
            else:
                return False
        if direct == "right":
            if self.x != WIDTH - 50:
                filtredbyy = [t for t in tilesArr if t.y == self.y]
                filtredbyx = [t for t in filtredbyy if t.x == self.x + 50]
                return filtredbyx[0]
            else:
                return False
        if direct == "up":
            if self.y != 0:
                filtredbyy = [t for t in tilesArr if t.y == self.y - 50]
                filtredbyx = [t for t in filtredbyy if t.x == self.x]
                return filtredbyx[0]
            else:
                return False
        if direct == "down":
            if self.y != HEIGHT - 50:
                filtredbyy = [t for t in tilesArr if t.y == self.y + 50]
                filtredbyx = [t for t in filtredbyy if t.x == self.x]
                return filtredbyx[0]
            else:
                return False
        if direct == "up-left":
            if self.x != 0 and self.y != 0:
                filtredbyy = [t for t in tilesArr if t.y == self.y - 50]
                filtredbyx = [t for t in filtredbyy if t.x == self.x - 50]
                return filtredbyx[0]
            else:
                return False
        if direct == "up-right":
            if self.x != WIDTH - 50 and self.y != 0:
                filtredbyy = [t for t in tilesArr if t.y == self.y - 50]
                filtredbyx = [t for t in filtredbyy if t.x == self.x + 50]
                return filtredbyx[0]
            else:
                return False
        if direct == "down-left":
            if self.x != 0 and self.y != HEIGHT - 50:
                filtredbyy = [t for t in tilesArr if t.y == self.y + 50]
                filtredbyx = [t for t in filtredbyy if t.x == self.x - 50]
                return filtredbyx[0]
            else:
                return False
        if direct == "down-right":
            if self.x != HEIGHT - 50 and self.y != HEIGHT - 50:
                filtredbyy = [t for t in tilesArr if t.y == self.y + 50]
                filtredbyx = [t for t in filtredbyy if t.x == self.x + 50]
                return filtredbyx[0]
            else:
                return False

    def left_click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            if self.num == 0:
                self.open_around_empty()
                open_empty_tiles()
            if self.num == 9:
                game_over()
            self.status = "open"

    def right_click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            if self.status != "open" and self.status != "flaged":
                self.status = "flaged"
                game_win()
            elif self.status == "flaged":
                self.status = "closed"

    def open_around_empty(self):
        filtredbyy = [t for t in tilesArr if t.y == self.y]
        t = [t for t in filtredbyy if t.x == self.x][0]
        if t.get_tile("left"):
            t.get_tile("left").status = "open"
        if t.get_tile("right"):
            t.get_tile("right").status = "open"
        if t.get_tile("up"):
            t.get_tile("up").status = "open"
        if t.get_tile("down"):
            t.get_tile("down").status = "open"
        if t.get_tile("up-left"):
            t.get_tile("up-left").status = "open"
        if t.get_tile("up-right"):
            t.get_tile("up-right").status = "open"
        if t.get_tile("down-right"):
            t.get_tile("down-right").status = "open"
        if t.get_tile("down-left"):
            t.get_tile("down-left").status = "open"

    def set_image_by_status(self):
        if self.status == "flaged":
            self.image = pygame.image.load('img/flag.png').convert_alpha()
        if self.status == "closed":
            self.image = pygame.image.load('img/tile.jpg').convert_alpha()
        if self.status == "open":
            if self.num == 0:
                self.image = pygame.image.load('img/tileopen.png')
            if self.num == 1:
                self.image = pygame.image.load('img/tileopen1.png')
            if self.num == 2:
                self.image = pygame.image.load('img/tileopen2.png')
            if self.num == 3:
                self.image = pygame.image.load('img/tileopen3.png')
            if self.num == 4:
                self.image = pygame.image.load('img/tileopen4.png')
            if self.num == 5:
                self.image = pygame.image.load('img/tileopen5.png')
            if self.num == 6:
                self.image = pygame.image.load('img/tileopen6.png')
            if self.num == 7:
                self.image = pygame.image.load('img/tileopen7.png')
            if self.num == 8:
                self.image = pygame.image.load('img/tileopen8.png')
            if self.num == 9:
                self.image = pygame.image.load('img/tileopen9.png')

    def update(self):
        self.set_image_by_status()
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)


tilesArr = [Tile() for i in range(ROWS * COLS)]


def get_coords():
    for y in range(COLS):
        for x in range(ROWS):
            yield x, y


coords = get_coords()

for tile in tilesArr:
    c = next(coords)
    tile.x = c[0] * 50
    tile.y = c[1] * 50

for tile in tilesArr:
    tiles.add(tile)


def set_bombs():
    counter = BOMBS
    while counter:
        y = randrange(ROWS) * 50
        x = randrange(COLS) * 50
        filtredbyy = [t for t in tilesArr if t.y == y]
        filtredbyx = [t for t in filtredbyy if t.x == x]
        if filtredbyx[0].num != 9:
            filtredbyx[0].num = 9
            counter = counter - 1


def place_nums():
    for t in tilesArr:
        if t.num != 9:
            if t.get_tile("left"):
                if t.get_tile("left").num == 9:
                    t.num = t.num + 1
            if t.get_tile("right"):
                if t.get_tile("right").num == 9:
                    t.num = t.num + 1
            if t.get_tile("up"):
                if t.get_tile("up").num == 9:
                    t.num = t.num + 1
            if t.get_tile("down"):
                if t.get_tile("down").num == 9:
                    t.num = t.num + 1
            if t.get_tile("up-left"):
                if t.get_tile("up-left").num == 9:
                    t.num = t.num + 1
            if t.get_tile("up-right"):
                if t.get_tile("up-right").num == 9:
                    t.num = t.num + 1
            if t.get_tile("down-right"):
                if t.get_tile("down-right").num == 9:
                    t.num = t.num + 1
            if t.get_tile("down-left"):
                if t.get_tile("down-left").num == 9:
                    t.num = t.num + 1


def change_stage(stage):
    global GAMESTAGE
    if stage == "game":
        GAMESTAGE = "game"
    if stage == "GAMEOVER":
        GAMESTAGE = "GAMEOVER"
    if stage == "WIN":
        GAMESTAGE = "WIN"


def game_over():
    for t in tilesArr:
        if t.num == 9:
            t.status = "open"
    change_stage("GAMEOVER")


def restart():
    for t in tilesArr:
        t.num = 0
        t.status = "closed"
    set_bombs()
    place_nums()
    change_stage("game")


def game_win():
    flags = 0
    for t in tilesArr:
        if t.status == "flaged" and t.num == 9:
            flags += 1
    if flags == BOMBS:
        change_stage("WIN")


def check_open_tiles(t):
    if t.get_tile("left"):
        if t.get_tile("left").status == "open" and t.get_tile("left").num == 0:
            return True
    if t.get_tile("right"):
        if t.get_tile("right").status == "open" and t.get_tile("right").num == 0:
            return True
    if t.get_tile("up"):
        if t.get_tile("up").status == "open" and t.get_tile("up").num == 0:
            return True
    if t.get_tile("down"):
        if t.get_tile("down").status == "open" and t.get_tile("down").num == 0:
            return True
    if t.get_tile("up-left"):
        if t.get_tile("up-left").status == "open" and t.get_tile("up-left").num == 0:
            return True
    if t.get_tile("up-right"):
        if t.get_tile("up-right").status == "open" and t.get_tile("up-right").num == 0:
            return True
    if t.get_tile("down-right"):
        if t.get_tile("down-right").status == "open" and t.get_tile("down-right").num == 0:
            return True
    if t.get_tile("down-left"):
        if t.get_tile("down-left").status == "open" and t.get_tile("down-left").num == 0:
            return True
    else:
        return False


def open_empty_tiles():
    changes = 1
    while changes:
        changes = 0
        for t in tilesArr:
            if t.num == 0 and t.status != "open":
                if check_open_tiles(t):
                    t.status = "open"
                    changes = 1

    for t in tilesArr:
        if t.status == "open" and t.num == 0:
            t.open_around_empty()


set_bombs()
place_nums()

running = True

while running:
    clock.tick(FPS)
    tiles.update()

    if GAMESTAGE == "game":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    for tile in tilesArr:
                        tile.left_click(event.pos)
                if event.button == 3:
                    for tile in tilesArr:
                        tile.right_click(event.pos)
        screen.fill("white")
        tiles.draw(screen)

    if GAMESTAGE == "GAMEOVER":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    restart()

        screen.fill("white")
        tiles.draw(screen)
        screen.blit(game_over_text, game_over_rect)
        screen.blit(restart_text, restart_rect)

    if GAMESTAGE == "WIN":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    restart()

        screen.fill("white")
        tiles.draw(screen)
        screen.blit(game_win_text, game_win_rect)
        screen.blit(restart_text, restart_rect)

    pygame.display.update()

pygame.quit()
