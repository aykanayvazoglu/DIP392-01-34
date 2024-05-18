
from sys import exit
import pygame

pygame.init()

screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption('Connect 4')
clock = pygame.time.Clock()

column_1 = pygame.Rect(292,0, 95, 720)
column_2 = pygame.Rect(392,0, 95, 720)
column_3 = pygame.Rect(492,0, 95, 720)
column_4 = pygame.Rect(592, 0, 95, 720)
column_5 = pygame.Rect(692,0, 95, 720)
column_6 = pygame.Rect(792,0, 95, 720)
column_7 = pygame.Rect(892,0, 95, 720)

background_surf = pygame.image.load('src/assets/bg.jpg').convert()

board_surf = pygame.image.load('src/assets/connect4Board.png').convert()
board_rect = board_surf.get_rect(midbottom=(640,720))

redtoken_surf = pygame.image.load('src/assets/redtoken.png')

bluetoken_surf = pygame.image.load('src/assets/bluetoken.png')

floor_rect = pygame.Rect(0, 709, 1280,11)

turn = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    turn = turn %2
    pygame.draw.rect(screen, (255,255,255), floor_rect)   
    pygame.draw.rect(screen, (0,0,0), column_1)
    pygame.draw.rect(screen, (0,0,0), column_2)
    pygame.draw.rect(screen, (0,0,0), column_3)
    pygame.draw.rect(screen, (0,0,0), column_4)
    pygame.draw.rect(screen, (0,0,0), column_5)
    pygame.draw.rect(screen, (0,0,0), column_6)
    pygame.draw.rect(screen, (0,0,0), column_7)     
    screen.blit(background_surf, (0,0))
    screen.blit(board_surf, board_rect)

    if(turn == 0):
        mouse_pos = pygame.mouse.get_pos()
        mouse_buttons = pygame.mouse.get_pressed()
        if column_1.collidepoint(mouse_pos):
            screen.blit(redtoken_surf, (292, 20))
            if mouse_buttons[0]:
                screen.blit(redtoken_surf, (300,floor_rect.top-83))
        elif  column_2.collidepoint(mouse_pos):
            screen.blit(redtoken_surf, (392, 20))
        elif  column_3.collidepoint(mouse_pos):
            screen.blit(redtoken_surf, (492, 20))
        elif  column_4.collidepoint(mouse_pos):
            screen.blit(redtoken_surf, (592, 20))
        elif  column_5.collidepoint(mouse_pos):
            screen.blit(redtoken_surf, (692, 20))
        elif  column_6.collidepoint(mouse_pos):
            screen.blit(redtoken_surf, (792, 20))
        elif  column_7.collidepoint(mouse_pos):
            screen.blit(redtoken_surf, (892, 20))
    pygame.display.update()
    clock.tick(60)
