import pygame

pygame.init()

window_width = 800
window_height = 600

white = (255, 255, 255)

# Images
background_image = pygame.image.load('images/icons/bg1.png')
play_icon = pygame.image.load('images/icons/play.png')
pause_icon = pygame.image.load('images/icons/pause.png')
next_icon = pygame.image.load('images/icons/next.png')
previous_icon = pygame.image.load('images/icons/next.png')

# Transforming
background_image = pygame.transform.scale(background_image, (800, 800))
play_icon = pygame.transform.scale(play_icon, (64, 64))
pause_icon = pygame.transform.scale(pause_icon, (64, 64))
next_icon = pygame.transform.scale(next_icon, (64, 64))
previous_icon = pygame.transform.scale(previous_icon, (64, 64))
previous_icon = pygame.transform.flip(previous_icon, True, False)

game_display = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Music Player')

font = pygame.font.SysFont(None, 36)

def draw(icon, x, y):
    game_display.blit(icon, (x, y))

def music_player():
    volume = 1
    playing = False
    paused = False
    current_song_index = 0
    songs = ["songs/Incepption_Time.mp3",
            "songs/Experience.mp3",
            "songs/Until_I_Found_You.mp3",
            "songs/Detroit.mp3",
            "songs/Interstellar.mp3"]  

    pygame.mixer.init()
    pygame.mixer.music.load(songs[current_song_index])

    panel_width = (next_icon.get_width() + play_icon.get_width() + previous_icon.get_width() + 50 * 2)
    panel_x = (window_width - panel_width) // 2

    while True:
        game_display.blit(background_image, (0, 0))
        
        draw(previous_icon, panel_x, 250)
        draw(play_icon if not playing else pause_icon, panel_x + previous_icon.get_width() + 50, 250)
        draw(next_icon, panel_x + previous_icon.get_width() + play_icon.get_width() + 100, 250)
        
        for event in pygame.event.get():
            pressed = pygame.key.get_pressed()
            if event.type == pygame.QUIT or pressed[pygame.K_ESCAPE]:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if panel_x <= mouse_x <= panel_x + panel_width and 250 <= mouse_y <= 250 + play_icon.get_height():
                    if panel_x <= mouse_x <= panel_x + previous_icon.get_width() and 250 <= mouse_y <= 250 + previous_icon.get_height():
                        current_song_index = (current_song_index - 1) % len(songs)
                        pygame.mixer.music.load(songs[current_song_index])
                        pygame.mixer.music.play()
                        playing = True
                        paused = False
                    elif panel_x + previous_icon.get_width() + 50 <= mouse_x <= panel_x + previous_icon.get_width() + play_icon.get_width() + 50 and 250 <= mouse_y <= 250 + play_icon.get_height():
                        if playing:
                            pygame.mixer.music.pause()
                            paused = True
                        else:
                            pygame.mixer.music.unpause() if paused else pygame.mixer.music.play()
                        playing = not playing
                        paused = False
                    elif (panel_x + previous_icon.get_width() + play_icon.get_width() + 100 <= mouse_x <= panel_x + panel_width and 250 <= mouse_y <= 250 + next_icon.get_height()):
                        current_song_index = (current_song_index + 1) % len(songs)
                        pygame.mixer.music.load(songs[current_song_index])
                        pygame.mixer.music.play()
                        playing = True
                        paused = False
            else:
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_RIGHT]:
                    current_song_index = (current_song_index + 1) % len(songs)
                    pygame.mixer.music.load(songs[current_song_index])
                    pygame.mixer.music.play()
                    playing = True
                    paused = False
                elif pressed[pygame.K_LEFT]:
                    current_song_index = (current_song_index - 1) % len(songs)
                    pygame.mixer.music.load(songs[current_song_index])
                    pygame.mixer.music.play()
                    playing = True
                    paused = False
                elif pressed[pygame.K_SPACE]:
                    if playing:
                        pygame.mixer.music.pause()
                        paused = True
                    else:
                        pygame.mixer.music.unpause() if paused else pygame.mixer.music.play()
                    playing = not playing
                    paused = False
                elif pressed[pygame.K_UP]:
                    volume += 0.1  
                    if volume > 1:
                        volume = 1
                    pygame.mixer.music.set_volume(volume)
                elif pressed[pygame.K_DOWN]:
                    volume -= 0.1 
                    if volume < 0:
                        volume = 0
                    pygame.mixer.music.set_volume(volume) 
                    
        pygame.display.update()

music_player()