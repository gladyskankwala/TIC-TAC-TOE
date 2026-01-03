import pygame
import sys

WIDTH, HEIGHT = 300 , 300
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC-TAC-TOE')

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit
    sys.exit()

if __name__ == '__main__':
    main()