import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 300 , 300
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC-TAC-TOE')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

board = [' '] * 9
player = 'X'
FONT = pygame.font.SysFont(None, 80)

def draw_lines():
    WIN.fill(WHITE)
    pygame.draw.line(WIN, BLACK, (100, 0), (100, 300), 3)
    pygame.draw.line(WIN, BLACK, (200, 0), (200, 300), 3)
    pygame.draw.line(WIN, BLACK, (0, 100), (300, 100), 3)
    pygame.draw.line(WIN, BLACK, (0, 200), (300, 200), 3)


def draw_symbols():
    for i in range(9):
        x = (i % 3 ) * 100 + 35
        y = (i // 3) * 100 + 25
        if board[i] != ' ':
            text = FONT.render(board[i] ,True, BLACK)
            WIN.blit(text, (x, y))

def check_winner(symbol):
    wins =[
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]

    for a,b,c in wins:
        if board[a] == board[b] == board[c]  == symbol:
            return True
    return False

def main():
    global player
    run = True
    while run:
        draw_lines()
        draw_symbols()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = event.pos
                index = (mouseY // 100) * 3 + (mouseX // 100)

                if board[index] == ' ':
                    board[index] = player

                    if check_winner(player):
                        print(f'player {player} wins')
                        run = False

                    player = "O" if player == 'X' else 'X'
        pygame.display.update()
    
    

if __name__ == '__main__':
    main()