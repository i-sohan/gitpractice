import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Player
player = pygame.Rect(WIDTH // 2 - 25, HEIGHT - 70, 50, 50)

# Bullet list
bullets = []

# Enemy list
enemies = []

score = 0
font = pygame.font.SysFont(None, 36)

enemy_timer = 0

running = True

while running:

    clock.tick(60)
    screen.fill(BLACK)

    # Events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = pygame.Rect(
                    player.centerx - 3,
                    player.top,
                    6,
                    15,
                )
                bullets.append(bullet)

    # Movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= 7

    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += 7

    # Spawn enemies
    enemy_timer += 1

    if enemy_timer > 30:
        enemy = pygame.Rect(
            random.randint(0, WIDTH - 40),
            -40,
            40,
            40,
        )
        enemies.append(enemy)
        enemy_timer = 0

    # Move bullets
    for bullet in bullets[:]:
        bullet.y -= 10

        if bullet.bottom < 0:
            bullets.remove(bullet)

    # Move enemies
    for enemy in enemies[:]:
        enemy.y += 4

        if enemy.top > HEIGHT:
            enemies.remove(enemy)

        if enemy.colliderect(player):
            running = False

    # Collision detection
    for bullet in bullets[:]:
        for enemy in enemies[:]:

            if bullet.colliderect(enemy):

                if bullet in bullets:
                    bullets.remove(bullet)

                if enemy in enemies:
                    enemies.remove(enemy)

                score += 1
                break

    # Draw player
    pygame.draw.rect(screen, GREEN, player)

    # Draw bullets
    for bullet in bullets:
        pygame.draw.rect(screen, WHITE, bullet)

    # Draw enemies
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

    # Score
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.flip()

pygame.quit()
