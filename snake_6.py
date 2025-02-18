import pygame
import time
import random

pygame.init()

screen = pygame.display.set_mode((600, 600))
game_icon = pygame.image.load('google_snake.jpg')
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Snake game - by Nathan Yew")

# Tuples containing the colours to be used in the game
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (188, 227, 199)
yellow = (255, 255, 0)

# Fonts for the game
score_font = pygame.font.SysFont("arialblack", 20)
exit_font = pygame.font.SysFont("freesansbold.ttf", 30)
msg_font = pygame.font.SysFont("arialblack", 20)


def message(msg, txt_colour, bkgd_colour):
    txt = msg_font.render(msg, True, txt_colour, bkgd_colour)

    # Centre rectangle: 600/2 = 300 and 600/2 = 300
    text_box = txt.get_rect(center=(300, 300))
    screen.blit(txt, text_box)


clock = pygame.time.Clock()

quit_game = False

# snake will be 20 x 20 pixels
snake_x = 290
snake_y = 290

snake_x_change = 0
snake_y_change = 0

# Setting a random position for the food to start
food_x = round(random.randrange(20, 600 - 20) / 20) * 20
food_y = round(random.randrange(20, 600 - 20) / 20) * 20

while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x_change = -20
                snake_y_change = 0
            if event.key == pygame.K_RIGHT:
                snake_x_change = 20
                snake_y_change = 0
            if event.key == pygame.K_UP:
                snake_x_change = 0
                snake_y_change = -20
            if event.key == pygame.K_DOWN:
                snake_x_change = 0
                snake_y_change = 20

    if snake_x >= 600 or snake_x < 0 or snake_y >= 600 or snake_y < 0:
        quit_game = True

    snake_x += snake_x_change
    snake_y += snake_y_change

    screen.fill(green)

    # Create rectangle for snake
    pygame.draw.rect(screen, red, [snake_x, snake_y, 20, 20])
    pygame.display.update()

    # Create circle for food
    pygame.draw.circle(screen, yellow, [food_x, food_y], 10)
    pygame.display.update()

    # Collision detection (test if snake touches food)
    if snake_x == food_x - 10 and snake_y == food_y - 10:
        # Set new random position for food if snake touches it
        food_x = round(random.randrange(20, 600 - 20) / 20) * 20
        food_y = round(random.randrange(20, 600 - 20) / 20) * 20

    clock.tick(35)

screen.fill(black)
message("You died!", red, black)
pygame.display.update()
time.sleep(3)

pygame.quit()
quit()
