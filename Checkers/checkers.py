import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE
from checkers.game import Game
#build module

#frame rate/fps
FPS = 60
#interface
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

#game name/title
pygame.display.set_caption("Checkers")

def get_mouse_row_col(pos):
    
    #unpack pos tuple into x, y
    x, y = pos

    #int divide x, y by SQUARE_SIZE to get no. of row, col
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()

    game = Game(WIN)
    
    #game loop
    while run:
        clock.tick(FPS)
        #event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                #get mouse position
                pos = pygame.mouse.get_pos()

                #unpack mouse position tuple into row, col
                row, col = get_mouse_row_col(pos)

                
        
        game.update()

    pygame.quit()

main()