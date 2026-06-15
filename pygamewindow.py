import pygame
pygame.init()
screen=pygame.display.set_mode((500,400))
pygame.display.set_caption('My first game window')
background=pygame.image.load('DJ Cat1.webp ')
character=pygame.image.load('indian greetings.png')
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.blit(background,(0,0))
    screen.blit(character,(200,200))     
pygame.display.update()
pygame.quit()