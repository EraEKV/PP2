import pygame
import datetime
import os
from sys import exit

pygame.init()

window_width = 829
window_height = 836
game_display = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()

bg = pygame.image.load(os.path.normpath('images/bg.png'))
hand_second = pygame.image.load(os.path.normpath('images/hand_second.png'))
hand_hour = pygame.image.load(os.path.normpath('images/hand_hour.png'))
rect = bg.get_rect(center=(415, 418))

while True:
    pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or pressed[pygame.K_ESCAPE]:
            pygame.quit()
            exit()
    time = datetime.datetime.now()
    
    # angles
    angle_hour = -(time.hour * 30 + time.minute / 2 + time.second / 120) 
    angle_minute = -(time.minute * 6 + time.second / 10)  
    angle_second = -(time.second * 6 + time.microsecond / 1000000 * 6)  
    
    game_display.blit(bg, (0, 0))
    
    # hours
    hand_hour_img = pygame.transform.rotate(hand_hour, angle_hour)
    hand_hour_rect = hand_hour_img.get_rect(center=rect.center)
    game_display.blit(hand_hour_img, hand_hour_rect.topleft)
    
    # seconds
    hand_second_img = pygame.transform.rotate(hand_second, angle_second)
    hand_second_rect = hand_second_img.get_rect(center=rect.center)
    game_display.blit(hand_second_img, hand_second_rect.topleft)
    
    pygame.display.flip()
    clock.tick(60)  

pygame.quit()
