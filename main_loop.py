import pygame
from sprites.spritesheet import SpriteSheet

pygame.init()
DISPLAY_W, DISPLAY_Y = 640, 640
canvas = pygame.Surface((DISPLAY_W, DISPLAY_Y))
screen = pygame.display.set_mode((DISPLAY_W, DISPLAY_Y))
clock = pygame.time.Clock()
running = True
dt = 0
y_velocity = 0
jump_strength = 6
gravity = 0.5
ground_level = 100
player_height = 40
player_speed = 2
player_pos = pygame.Vector2(0,0)

try:
    background_image = pygame.image.load('pixel-mountain.png').convert()
except pygame.error as e:
    print(f"Error loading image: {e}")
    pygame.quit()
    exit()

idle_spritesheet = SpriteSheet('sprites/Idle')
idle_hiker = [
    idle_spritesheet.parse_sprite('idle_hiker_1'),
    idle_spritesheet.parse_sprite('idle_hiker_2'),
    idle_spritesheet.parse_sprite('idle_hiker_3'),
    idle_spritesheet.parse_sprite('idle_hiker_4'),
    idle_spritesheet.parse_sprite('idle_hiker_5'),
    idle_spritesheet.parse_sprite('idle_hiker_6')
]

run_spritesheet = SpriteSheet('sprites/Run')
run_hiker = [
    run_spritesheet.parse_sprite('run_hiker_1'),
    run_spritesheet.parse_sprite('run_hiker_2'),
    run_spritesheet.parse_sprite('run_hiker_3'),
    run_spritesheet.parse_sprite('run_hiker_4'),
    run_spritesheet.parse_sprite('run_hiker_5'),
    run_spritesheet.parse_sprite('run_hiker_6')
]

flying_spritesheet = SpriteSheet('sprites/Flying')
flying_hiker = [
    flying_spritesheet.parse_sprite('flying_hiker_1'),
    flying_spritesheet.parse_sprite('flying_hiker_2')
]

jumping_spritesheet = SpriteSheet('sprites/Jump')
jumping_hiker = [
    jumping_spritesheet.parse_sprite('jump_hiker_1'),
    jumping_spritesheet.parse_sprite('jump_hiker_2')
]

current_idle_index = 0
current_run_index = 0
current_flying_index = 0
current_jump_index = 0
animation_timer = 0
animation_speed = 100
zoom_factor = 2.5

while running:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    animation_timer += dt

    if animation_timer >= animation_speed:
        animation_timer = 0
        current_idle_index = (current_idle_index + 1) % len(idle_hiker)
        current_run_index = (current_run_index + 1) % len(run_hiker)
        current_flying_index = (current_flying_index + 1) % len(flying_hiker)
        current_jump_index = (current_jump_index + 1) % len(jumping_hiker)

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

    animation = 'idle'
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player_pos.x += player_speed
        animation = 'running'
    if keys[pygame.K_LEFT]:
        player_pos.x -= player_speed
        animation = 'running'
    if keys[pygame.K_a]:
        player_pos.x -= player_speed
        animation = 'running'
    if keys[pygame.K_d]:
        player_pos.x += player_speed
        animation = 'running'
    if keys[pygame.K_SPACE] and y_velocity == 0:
        y_velocity = -jump_strength
    
    y_velocity += gravity
    player_pos.y += y_velocity

    if player_pos.y >= screen.get_height() - ground_level - player_height:
        player_pos.y = screen.get_height() - ground_level - player_height
        y_velocity = 0
    
    # if player_cir.colliderect(obstacle_1) or player_cir.colliderect(obstacle_2):
    #     y_velocity = 0

    current_player_image = idle_hiker[current_idle_index]
    if animation == 'running':
        current_player_image = run_hiker[current_run_index]
    if y_velocity > 0:
        current_player_image = flying_hiker[current_flying_index]
    if y_velocity < 0:
        current_player_image = jumping_hiker[current_jump_index]

    new_width = int(background_image.get_width() * zoom_factor)
    new_height = int(background_image.get_height() * zoom_factor)
    zoomed_background = pygame.transform.smoothscale(background_image, (new_width, new_height))
    # offset_x = (new_width - DISPLAY_W) // 2
    # offset_y = (new_height - DISPLAY_Y) // 2
    offset_x = player_pos.x
    offset_y = player_pos.y
    
    player_width = current_player_image.get_width() * 2
    player_height = current_player_image.get_height() * 2
    scaled_current_player = pygame.transform.scale(current_player_image, (player_width, player_height))
    canvas.blit(zoomed_background, (-offset_x, -offset_y))
    canvas.blit(scaled_current_player, (player_pos.x, player_pos.y))
    
    screen.blit(canvas, (0,0))
    pygame.display.update()
    pygame.display.flip()
    

pygame.quit()