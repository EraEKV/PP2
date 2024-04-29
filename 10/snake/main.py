import pygame
import sys
import time
import pygame_menu
import random
import datetime
import psycopg2 
from config import database, host, user, password
pygame.init()



# DB contains table with properties id, username, score, pos 


# Trying to connect database
try:
    connection = psycopg2.connect(
        host = host,
        database = database,
        user = user,
        password = password
    )
    
    connection.autocommit = True  # for autocommiting all changes  
    
    # curs = connection.cursor()

    with connection.cursor() as curs:
        curs.execute(
            "SELECT version();"
        )
        print(f"server version: {curs.fetchone()}")
    
    
    # Creating a table users with properties id, username, score and pos 
    with connection.cursor() as curs:
        curs.execute(
            """CREATE TABLE users(
                    id SERIAL PRIMARY KEY,
                    username varchar(50) NOT NULL,
                    score int DEFAULT 0,
                    last_score int DEFAULT 0,
                    pos varchar(6) DEFAULT '1,0',
                    dir varchar(5) DEFAULT '1,0'
                )"""
        )
        connection.commit()
        print("[INFO] Table created")
    
    
    with connection.cursor() as curs:
        # curs.execute("DELETE FROM users WHERE username = 'username'")
        curs.execute("SELECT * FROM users")
        print(curs.fetchall()[0])
    
except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
# finally:
#     if connection:
#         connection.close()
#         print("[INFO] PostreSQL connection closed")





# Basic constants
SW, SH = 800, 800

BLOCK_SIZE = 40
FONT = pygame.font.SysFont("consolas", int(BLOCK_SIZE / 2))


# Game variables
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Snake Adventures")
clock = pygame.time.Clock()
difficulty = 10
color = "black"
# LEVELS = ["Beginner", "Easy", "Medium", "Hard", "Master", "Hardcore"]

score = FONT.render("0", True, "white")
score_rect = score.get_rect(center = (SW / 20, SH / 20))

lvl_change = 3
level = FONT.render("1", True, "white")
level_rect = level.get_rect(center = (SW - 100, SH / 20))


disappear = 3000
disappear_timer = -1

name = "username"



# Snake class
class Snake:
    def __init__(self):
        self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
        self.xdir = 1
        self.ydir = 0
        self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
        self.body = [pygame.Rect(self.x - BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]
        self.dead = False

    def update(self):
        # Collision logic
        for square in self.body:
            if self.head.x == square.x and self.head.y == square.y:
                self.dead = True
            if self.head.x not in range(0, SW) or self.head.y not in range(0, SH):
                self.dead = True
        
        
        # Game over
        if self.dead:
            with connection.cursor() as curs:
                print(name)
                curs.execute(f"SELECT score FROM users WHERE username = '{name}'")
                all_score = int(curs.fetchall()[0][0]) + len(self.body) - 1
                print(all_score, type(all_score))
                curs.execute(f"UPDATE users SET score = '{all_score}', last_score = {0}, pos = '1,0', dir = '1,0' WHERE username = '{name}'")
                # data = curs.fetchall()
            pygame.mixer.Sound('died.mp3').play()        
            
            my_font = pygame.font.SysFont('times new roman', 90)
            game_over_surface = my_font.render('YOU DIED', True, "red")
            game_over_rect = game_over_surface.get_rect()
            game_over_rect.midtop = (SW / 2, SH / 4)
            screen.fill("black")
            screen.blit(game_over_surface, game_over_rect)
            
            score_surface = pygame.font.SysFont("consolas", int(40)).render(f'Score: {all_score}', True, "red")
            score_rect = score_surface.get_rect()
            score_rect.topleft = (300, SH / 2) 
            screen.blit(score_surface, score_rect)

            level_surface = pygame.font.SysFont("consolas", int(40)).render(f'Level: {int((len(snake.body) - 1) / lvl_change + 1)}', True, "red")
            level_rect = level_surface.get_rect()
            level_rect.topleft = (300, 500) 
            screen.blit(level_surface, level_rect)

            

            # global LEVELS            
            # lvl_surface = pygame.font.SysFont("consolas", int(40)).render(f'{LEVELS[int((len(snake.body) - 1) / lvl_change)]}', True, "red")
            # lvl_rect = lvl_surface.get_rect()
            # lvl_rect.topleft = (300, 550) 
            # screen.blit(lvl_surface, lvl_rect)

            pygame.display.update()  
            pygame.display.flip()
            time.sleep(6)
            pygame.quit()
            sys.exit()


        # Different levels
        global difficulty, color, disappear
        if (len(self.body) - 1) % lvl_change == 0 and int((len(snake.body) - 1) / lvl_change + 1) == 2:
            color = "grey"
            difficulty = 15
            disappear = 3000
        elif (len(self.body) - 1) % lvl_change == 0 and int((len(snake.body) - 1) / lvl_change + 1) == 3:
            color = "blue"
            difficulty = 20
            disappear = 2500
        elif (len(self.body) - 1) % lvl_change == 0 and int((len(snake.body) - 1) / lvl_change + 1) == 4:
            color = "aqua"
            difficulty = 25
            disappear = 2000
        elif (len(self.body) - 1) % lvl_change == 0 and int((len(snake.body) - 1) / lvl_change + 1) == 5:
            color = "brown"
            difficulty = 30
            disappear = 1500
        elif (len(self.body) - 1) % lvl_change == 0 and int((len(snake.body) - 1) / lvl_change + 1) == 6:
            color = "green"
            difficulty = 45
            disappear = 800
        
        self.body.append(self.head)
        for i in range(len(self.body) - 1):
            self.body[i].x, self.body[i].y = self.body[i + 1].x, self.body[i + 1].y
        self.head.x += self.xdir * BLOCK_SIZE
        self.head.y += self.ydir * BLOCK_SIZE
        self.body.remove(self.head)
        
        # Starting a new game code  
        # if self.dead:
        #     global food
        #     self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
        #     self.xdir = 1
        #     self.ydir = 0
        #     self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
        #     self.body = [pygame.Rect(self.x - BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]
        #     self.dead = False
        #     food = Food()



# Food class
class Food:
    def __init__(self):
        self.x = int(random.randint(0, SW) / BLOCK_SIZE) * BLOCK_SIZE
        self.y = int(random.randint(0, SH) / BLOCK_SIZE) * BLOCK_SIZE
        self.rect = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
        
    def update(self):
        pygame.draw.rect(screen, "red", self.rect)

class Bonus:
    def __init__(self):
        self.x = int(random.randint(0, SW - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
        self.y = int(random.randint(0, SH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
        # self.positions = [[self.x, self.x + 1], [self.y, self.y + 1]]
        self.rect = pygame.Rect(self.x, self.y, BLOCK_SIZE * 2, BLOCK_SIZE * 2)

    def update(self):
        pygame.draw.rect(screen, "blue", self.rect)
    
    
    
# Func drawing game grid
def grid():
    for x in range(0, SW, BLOCK_SIZE):
        for y in range(0, SH, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, "#3c3c3b", rect, 1)
        
grid()        
    
    
# Creating instance for snake and food classes
# snake = Snake()
# food = Food()
# bonus = Bonus()

# flag = False



def save():
    print(name)
    with connection.cursor() as curs:
        print(snake.head.x / BLOCK_SIZE)
        print(f"{snake.head.x / BLOCK_SIZE},{snake.head.y / BLOCK_SIZE}")
        curs.execute(f"UPDATE users SET last_score = '{len(snake.body) - 1}', pos = '{int(snake.head.x / BLOCK_SIZE)},{int(snake.head.y / BLOCK_SIZE)}', dir = '{snake.xdir},{snake.ydir}' WHERE username = '{name}'")
        print("[INFO] Saved successfully!")
        curs.execute(f"SELECT * FROM users WHERE username = '{name}'")
        print(curs.fetchall())
    

# Game function
# flag = False
def Game() -> None:
    snake = Snake()
    food = Food()
    bonus = Bonus()

    # global food
    # global disappear_timer
    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Movement logic
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu = pygame_menu.Menu('Pause', 800, 800, theme=pygame_menu.themes.THEME_DARK)
                    menu.add.button('Resume', Game)
                    menu.add.button('Save', save)
                    menu.add.button('Quit', pygame_menu.events.EXIT)
                    menu.mainloop(screen)
                    # pygame.quit()
                    # sys.exit() 
                    
                if (event.key == pygame.K_s or event.key == pygame.K_DOWN) and snake.ydir != -1:
                    snake.xdir = 0
                    snake.ydir = 1
                elif (event.key == pygame.K_w or event.key == pygame.K_UP) and snake.ydir != 1:
                    snake.xdir = 0
                    snake.ydir = -1
                elif (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and snake.xdir != -1:
                    snake.xdir = 1
                    snake.ydir = 0
                elif (event.key == pygame.K_a or event.key == pygame.K_LEFT) and snake.xdir != 1:
                    snake.xdir = -1
                    snake.ydir = 0
                
        snake.update()
        
        screen.fill(color)
        grid()
            

        if len(snake.body) % 21 == 0:
            bonus.update()
            cur = pygame.time.get_ticks()
            if disappear_timer == -1: disappear_timer = pygame.time.get_ticks()
            if cur - disappear_timer > disappear:
                food = Food()
                snake.body.append(pygame.Rect(square.x, square.y, BLOCK_SIZE, BLOCK_SIZE))  
                disappear_timer = -1
        else:
            food.update()
        
        score = FONT.render(f"Score: {len(snake.body) - 1}", True, "white")
        level = FONT.render(f"Level: {int((len(snake.body) - 1) / lvl_change + 1)}", True, "white")

        pygame.draw.rect(screen, "green", snake.head)
        
        for square in snake.body:
            pygame.draw.rect(screen, "green", square)

        screen.blit(score, score_rect)
        screen.blit(level, level_rect)

        # Eating food logic
        if snake.head.x == food.x and snake.head.y == food.y:
            snake.body.append(pygame.Rect(square.x, square.y, BLOCK_SIZE, BLOCK_SIZE))
            food = Food()
        if (snake.head.x - 1 == bonus.x or snake.head.x == bonus.x ) and (snake.head.y == bonus.y - 1 or snake.head.y == bonus.y):
            snake.body.append(pygame.Rect(square.x, square.y, BLOCK_SIZE, BLOCK_SIZE))
            snake.body.append(pygame.Rect(square.x, square.y, BLOCK_SIZE, BLOCK_SIZE))
            snake.body.append(pygame.Rect(square.x, square.y, BLOCK_SIZE, BLOCK_SIZE))
            food = Food()

        
        
        pygame.display.update()
        clock.tick(difficulty)
    

def auth_wrapper():
    global name 
    name = name_box.get_value()
    auth(name)

def auth(name):
    global snake
    if name != 'username':
        with connection.cursor() as curs:
            print(name)
            curs.execute(f"SELECT * FROM users WHERE username = '{name}'")
            data = curs.fetchall()
            if data:
                print(data[0])
                print("[INFO] User exists")
                
                pos = data[0][4].split(",")
                snake.head.x = int(pos[0]) * BLOCK_SIZE
                snake.head.y = int(pos[1]) * BLOCK_SIZE
                
                for i in range(data[0][3]):
                    snake.body.append(pygame.Rect(snake.body[-1].x, snake.body[-1].y, BLOCK_SIZE, BLOCK_SIZE))
                    
                dir = data[0][5].split(",")
                snake.xdir = int(dir[0])
                snake.ydir = int(dir[1])
                Game()
            else:
                print("not exist")
                curs.execute(f"INSERT INTO users (username) VALUES ('{name}') RETURNING *")
                print("[INFO] User created")
                Game()

menu = pygame_menu.Menu('Welcome', 800, 800, theme=pygame_menu.themes.THEME_DARK)

name_box = menu.add.text_input('Name:', default='username')
menu.add.button('Play', auth_wrapper)
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(screen)


