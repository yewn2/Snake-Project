import pygame
import time
pygame.init()

screen = pygame.display.set_mode((1000, 650))
game_icon = pygame.image.load('google_snake.jpg')
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Snake game - by Nathan Yew")


# Tuples containing the colours to be used in the game
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (188, 227, 199)

# Fonts for the game
score_font = pygame.font.SysFont("arialblack", 20)
exit_font = pygame.font.SysFont("freesansbold.ttf", 30)

clock = pygame.time.Clock()

quit_game = False

# snake will be 20 x 20 pixels
snake_x = 490
snake_y = 350

snake_x_change = 0
snake_y_change = 0

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

    snake_x += snake_x_change
    snake_y += snake_y_change

    screen.fill(green)

    # Create rectangle for snake
    pygame.draw.rect(screen, red, [snake_x, snake_y, 20, 20])
    pygame.display.update()

    clock.tick(35)

pygame.quit()
quit()
