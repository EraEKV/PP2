import pygame
from random import shuffle


def play_music(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(f"./songs/{file_path}")
    pygame.mixer.music.play(0)

def stop_music():
    pygame.mixer.music.stop()

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


def program(width, height):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('press space to see next demo')
    background = create_background(width, height)
    song_paths = [
        "Incepption_Time.mp3",
        "Experience.mp3",
        "Until_I_Found_You.mp3",
        "Detroit.mp3",
        "Interstellar.mp3"
    ]
    
    current_song = 0
    
    while current_song < len(song_paths):
        pressed_keys = pygame.key.get_pressed()
        # command = input("Enter a command (play, stop, next, previous, quit): ").lower()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    current_song = (current_song + 1) 
                    # current_song = (current_song + 1) % len(file_paths)
                    play_music(song_paths[current_song])
                elif event.key == pygame.K_r:
                    play_music(song_paths[current_song])
                elif event.key == pygame.K_q or event.key == pygame.QUIT or pressed_keys[pygame.K_LALT] or pressed_keys[pygame.K_RALT] and event.type == pygame.KEYDOWN and event.key == pygame.K_F4 :
                    pygame.quit()
                    return

    pygame.quit()

if __name__ == "__main__":
    program(500, 500)

