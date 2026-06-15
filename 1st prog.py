# Import Necessary Libraries
import pygame

# Initialize required modules
pygame.init()

# Setup window geometry
screen = pygame.display.set_mode((400,500))

# Create a loop to run till the game is quit by the user
done = False

while not done:

    # Clear the event queue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # Make the changes visible
    pygame.display.flip()
    # adding image and background image
    import pygame
    pygame.init()
    screen=pygame.display.set_mode((500,500))
    pygame.display.set_caption('Adding image and background image') 
    background=pygame.image.load('DJ Cat1.webp')
    character=pygame.image.load('indian greetings.png')
    running=True 
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        screen.blit(background,(0,0))
        screen.blit(character,(150,150))
      
    pygame.quit()
