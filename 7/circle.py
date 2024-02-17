import pygame
import math


def create_background(width, height):
    colors = [(255, 255, 255), (212, 212, 212)]
    background = pygame.Surface((width, height))
    tile_width = 20
    y = 0
    while y < height:
            x = 0
            while x < width:
                    row = y // tile_width
                    col = x // tile_width
                    pygame.draw.rect(
                            background, 
                            colors[(row + col) % 2],
                            pygame.Rect(x, y, tile_width, tile_width))
                    x += tile_width
            y += tile_width
    return background
    

def is_trying_to_quit(event):
        pressed_keys = pygame.key.get_pressed()
        alt_pressed = pressed_keys[pygame.K_LALT] or pressed_keys[pygame.K_RALT]
        x_button = event.type == pygame.QUIT
        altF4 = alt_pressed and event.type == pygame.KEYDOWN and event.key == pygame.K_F4
        escape = event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
        return x_button or altF4 or escape


def run_demos(width, height, fps):
        pygame.init()
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('press space to see next demo')
        background = create_background(width, height)
        clock = pygame.time.Clock()
        demos = [
                do_circle_demo
                ]
        the_world_is_a_happy_place = 0
        while True:
                the_world_is_a_happy_place += 1
                for event in pygame.event.get():
                        if is_trying_to_quit(event):
                                return
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                                demos = demos[1:]
                screen.blit(background, (0, 0))
                if len(demos) == 0:
                        return
                demos[0](screen, the_world_is_a_happy_place)
                pygame.display.flip()
                clock.tick(fps)
                
                

def do_circle_demo(surface, counter):
        x = surface.get_width() // 2
        y = surface.get_height() // 2
        max_radius = min(x, y) * 4 // 5
        radius = abs(int(math.sin(counter * 3.14159 * 2 / 200) * max_radius)) + 1
        color = (0, 140, 255) # aquamarine
        
        # Draw a circle
        pygame.draw.circle(surface, color, (x, y), radius)


run_demos(400, 300, 60)

# pygame.draw.circle(surface, color, (50, 50), 25)