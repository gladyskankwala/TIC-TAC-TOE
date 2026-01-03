import pygame
import sys

WIDTH, HEIGHT = 300 , 300
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC-TAC-TOE')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw_lines():
    WIN.fill(WHITE)
    pygame.draw.line(WIN, BLACK, (100, 0), (100, 300), 3)
    pygame.draw.line(WIN, BLACK, (200, 0), (200, 300), 3)


def main():
    run = True
    while run:
        draw_lines()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        pygame.display.update()
    pygame.quit
    sys.exit()

if __name__ == '__main__':
    main()