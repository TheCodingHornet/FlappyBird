import pygame
import random
import os

# Configuration
pygame.init()
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FPS = 60

# Chemins des images
current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, 'assets')

def load_image(file, size=None):
    image = pygame.image.load(os.path.join(assets_path, file)).convert_alpha()
    return pygame.transform.scale(image, size) if size else image

# Chargement avec redimensionnement
bird_size = (30, 30)
pipe_size = (50, 400)
ground_size = (WIDTH, 50)
bg_size = (WIDTH, HEIGHT)

bg_image = load_image('background.png', bg_size)
ground_image = load_image('ground.png', ground_size)
pipe_image = load_image('pipe.png', pipe_size)
bird_images = [
    load_image('bird1.png', bird_size),
    load_image('bird2.png', bird_size),
    load_image('bird3.png', bird_size)
]

# Variables de défilement
bg_x = 0
ground_x = 0
scroll_speed = 1
ground_scroll_speed = 4

# Oiseau
bird_index = 0
bird_surf = bird_images[bird_index]
bird_rect = bird_surf.get_rect(center=(50, HEIGHT/2))
BIRDFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRDFLAP, 200)
bird_movement = 0
gravity = 0.25

# Tuyaux
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)

# Score
game_active = False
score = 0
font = pygame.font.Font(None, 40)

def draw_bg():
    screen.blit(bg_image, (bg_x, 0))
    screen.blit(bg_image, (bg_x + WIDTH, 0))

def draw_ground():
    screen.blit(ground_image, (ground_x, HEIGHT - 50))
    screen.blit(ground_image, (ground_x + WIDTH, HEIGHT - 50))

def create_pipe():
    random_gap = random.randint(150, 250)
    random_height = random.randint(200, HEIGHT - 200)

    bottom_pipe = pipe_image.get_rect(midtop=(WIDTH + 50, random_height + random_gap//2))
    top_pipe = pipe_image.get_rect(midbottom=(WIDTH + 50, random_height - random_gap//2))

    return bottom_pipe, top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 4
    return [pipe for pipe in pipes if pipe.right > -50]

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= HEIGHT:
            screen.blit(pipe_image, pipe)
        else:
            flipped_pipe = pygame.transform.flip(pipe_image, False, True)
            screen.blit(flipped_pipe, pipe)

def check_collision():
    for pipe in pipe_list:
        if bird_rect.colliderect(pipe):
            return False
    if bird_rect.top <= -20 or bird_rect.bottom >= HEIGHT - 50:
        return False
    return True

def rotate_bird(bird):
    return pygame.transform.rotozoom(bird, -bird_movement * 3, 1)

def display_score():
    score_surf = font.render(f'Score: {int(score)}', True, (255, 255, 255))
    screen.blit(score_surf, (10, 10))

def game_over_screen():
    # Fond semi-transparent
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 128))
    screen.blit(overlay, (0, 0))

    if score == 0:
        # Écran de démarrage
        start_text = font.render('Appuyez sur ESPACE pour commencer', True, (255, 255, 255))
        screen.blit(start_text, (WIDTH//2 - start_text.get_width()//2, HEIGHT//2))
    else:
        # Écran de game over
        game_over_text = font.render('Game Over!', True, (255, 0, 0))
        restart_text = font.render('Appuyez sur ESPACE pour rejouer', True, (255, 255, 255))
        score_text = font.render(f'Score: {int(score)}', True, (255, 255, 255))

        screen.blit(game_over_text, (WIDTH//2 - game_over_text.get_width()//2, HEIGHT//3))
        screen.blit(restart_text, (WIDTH//2 - restart_text.get_width()//2, HEIGHT//2))
        screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, HEIGHT//2 + 50))

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game_active:
                    bird_movement = -7
                else:
                    game_active = True
                    pipe_list.clear()
                    bird_rect.center = (50, HEIGHT/2)
                    bird_movement = 0
                    score = 0

        if event.type == SPAWNPIPE and game_active:
            pipe_list.extend(create_pipe())

        if event.type == BIRDFLAP:
            bird_index = (bird_index + 1) % 3
            bird_surf = bird_images[bird_index]

    # Défilement uniquement pendant le jeu
    if game_active:
        bg_x -= scroll_speed
        if bg_x <= -WIDTH:
            bg_x = 0

        ground_x -= ground_scroll_speed
        if ground_x <= -WIDTH:
            ground_x = 0

    # Affichage des éléments
    draw_bg()

    if game_active:
        # Mouvement de l'oiseau
        bird_movement += gravity
        bird_rect.centery += bird_movement
        rotated_bird = rotate_bird(bird_surf)
        screen.blit(rotated_bird, bird_rect)

        # Gestion des tuyaux
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)
        game_active = check_collision()
        score += 0.0167

    draw_ground()
    display_score()

    # Affichage des écrans de statut
    if not game_active:
        game_over_screen()

    pygame.display.update()
    clock.tick(FPS)