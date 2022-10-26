import pygame
import random

WIDTH = 800
HEIGHT = 800
ROWS = 16
COLS = 16
FPS = 30

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

tiles = pygame.sprite.Group()


class Tile(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/tile.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.topleft = (self.x, self.y)

    def update(self):
        self.rect.topleft = (self.x, self.y)


tilesArr = [Tile() for i in range(256)]


def get_coords():
    for y in range(COLS):
        for x in range(ROWS):
            yield x, y


coords = get_coords()

for tile in tilesArr:
    c = next(coords)
    tile.x = c[0]*50
    tile.y = c[1]*50

for tile in tilesArr:
    print([tile.y, tile.x])

for tile in tilesArr:
    tiles.add(tile)

# Цикл игры
running = True

while running:
    clock.tick(FPS)
    tiles.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    tiles.draw(screen)
    pygame.display.update()

pygame.quit()
