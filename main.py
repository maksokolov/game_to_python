import pygame
import random
import os



WIDTH = 1200
HEIGHT = 800
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255 ,0, 0)
GREEN = (0, 0, 255)
BLUE = (0 , 0, 255)

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tanks go")
clock = pygame.time.Clock()

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
player_img = pygame.image.load(os.path.join(img_folder, 'ms-min.png')).convert()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.right = 0

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.update()

    screen.fill(BLUE)
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()
