import pygame, sys
from pygame.locals import QUIT

clock = pygame.time.Clock()

screen = pygame.display.set_mode((800, 600))

pygame.init()

pygame.display.set_caption("Jogo teste")

anim_time = 0
c_frame = 0
hero_walk_list = []

for i in range(4):
    hero_walk_list.append(pygame.image.load(f"assets/Hero_Walk_0{i + 1}.png"))

while True:
    for ev in pygame.event.get():
        if pygame.event == QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(60)
    dt = clock.get_time()


    c_frame = c_frame + 1
    if c_frame > len(hero_walk_list) - 1:
        c_frame = 0