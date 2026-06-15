import pygame

# Initialize Pygame
pygame.init()

# Create game window
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Pygame Events")

# Game loop
running = True
while running:

    # Check events
    for event in pygame.event.get():

        # Close button event
        if event.type == pygame.QUIT:
            print("Window Closed")
            running = False

        # Keyboard event
        if event.type == pygame.KEYDOWN:
            print("A key was pressed!")

        # Mouse click event
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Mouse clicked!")

    # Fill screen with white color
    screen.fill((255, 255, 255))

    # Update display
    pygame.display.update()

# Quit Pygame
pygame.quit()