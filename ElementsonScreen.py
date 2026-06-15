import pygame

# Initialize pygame
pygame.init()

# Create screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Shapes in PyGame")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Main loop
running = True
while running:
    screen.fill(WHITE)

    # Draw Rectangle
    pygame.draw.rect(screen, BLUE, (50, 100, 200, 100))

    # Draw Square
    pygame.draw.rect(screen, GREEN, (300, 100, 100, 100))

    # Draw Solid Ball (Circle)
    pygame.draw.circle(screen, RED, (600, 150), 50)

    # Update display
    pygame.display.update()

    # Check for quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()