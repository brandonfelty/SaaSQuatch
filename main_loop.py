import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
y_velocity = 0
jump_strength = 20
gravity = 0.5
ground_level = 100
player_height = 40
player_pos = pygame.Vector2(200, ground_level)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('blue')
    pygame.draw.circle(screen, "red", player_pos, player_height)
    pygame.draw.rect(screen, "black", [200, 300, 100, 20], 2)
    pygame.draw.rect(screen, "black", [800, 300, 100, 20], 2)
    pygame.draw.line(
        screen, "green",
        [0, screen.get_height() - ground_level],
        [screen.get_width(), screen.get_height() - ground_level],
        4
    )

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

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()