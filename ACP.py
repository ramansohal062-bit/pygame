import pygame

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rectangle Movement Game")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Rectangle 1 (movable)
rect1 = pygame.Rect(100, 100, 100, 60)

# Rectangle 2 (fixed)
rect2 = pygame.Rect(500, 300, 120, 80)

# Movement speed
speed = 5

# Game loop
running = True
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key controls
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        rect1.x -= speed
    if keys[pygame.K_RIGHT]:
        rect1.x += speed
    if keys[pygame.K_UP]:
        rect1.y -= speed
    if keys[pygame.K_DOWN]:
        rect1.y += speed

    # Fill background
    screen.fill(WHITE)

    # Draw rectangles
    pygame.draw.rect(screen, BLUE, rect1)
    pygame.draw.rect(screen, RED, rect2)

    # Update display
    pygame.display.update()

# Quit Pygame
pygame.quit()