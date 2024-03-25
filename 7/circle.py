import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

x, y = 400, 400
delta = 0

while True:
    pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or pressed[pygame.K_ESCAPE]:
            pygame.quit()
            exit()

    if pressed[pygame.K_UP] and y >= 27:
        y -= 20
    if pressed[pygame.K_DOWN] and y <= 765.5:
        y += 20
    if pressed[pygame.K_LEFT] and x >= 27:
        x -= 20
    if pressed[pygame.K_RIGHT] and x <= 765.5:
        x += 20

    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (255, 0, 0), (x, y), 25)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
