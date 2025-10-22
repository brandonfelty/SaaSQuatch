import pygame
from sprites.spritesheet import SpriteSheet

pygame.init()
DISPLAY_W, DISPLAY_Y = 1280, 720
canvas = pygame.Surface((DISPLAY_W, DISPLAY_Y))
screen = pygame.display.set_mode((DISPLAY_W, DISPLAY_Y))
clock = pygame.time.Clock()
running = True
dt = 0
y_velocity = 0
jump_strength = 20
gravity = 0.5
ground_level = 100
player_height = 40
player_pos = pygame.Vector2(200, ground_level)

idle_spritesheet = SpriteSheet('sprites/Idle.png')
hiker = idle_spritesheet.get_sprite(0,0,128,128)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    canvas.fill((255,255,255))
    canvas.blit(hiker, (0, DISPLAY_Y - 128))
    screen.blit(canvas, (0,0))
    pygame.display.update()

    # screen.fill('blue')
    # hiker = canvas.blit
    # player_cir = pygame.draw.circle(screen, "red", player_pos, player_height)
    # obstacle_1 = pygame.draw.rect(screen, "black", [200, 300, 100, 20], 2)
    # obstacle_2 = pygame.draw.rect(screen, "black", [800, 300, 100, 20], 2)
    # pygame.draw.line(
    #     screen, "green",
    #     [0, screen.get_height() - ground_level],
    #     [screen.get_width(), screen.get_height() - ground_level],
    #     4
    # )

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player_pos.x += 300 * dt
    if keys[pygame.K_LEFT]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
    if keys[pygame.K_SPACE] and y_velocity == 0:
        y_velocity = -jump_strength
    
    y_velocity += gravity
    player_pos.y += y_velocity

    if player_pos.y >= screen.get_height() - ground_level - player_height:
        player_pos.y = screen.get_height() - ground_level - player_height
        y_velocity = 0
    
    # if player_cir.colliderect(obstacle_1) or player_cir.colliderect(obstacle_2):
    #     y_velocity = 0

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()