from sys import exit
import pygame
import numpy as np

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

background_surf = pygame.image.load('assets/bg.jpg').convert()

window_icon = pygame.image.load('assets/icon.png')
pygame.display.set_icon(window_icon)

board_surf = pygame.image.load('assets/connect4Board.png').convert()
board_rect = board_surf.get_rect(midbottom=(640,720))

redtoken_surf = pygame.image.load('assets/redtoken.png')

bluetoken_surf = pygame.image.load('assets/bluetoken.png')

floor_rect = pygame.Rect(0, 709, 1280,11)

game_board = np.full((6, 7), 6)
col1_pressed = 0
col2_pressed = 0
col3_pressed = 0
col4_pressed = 0
col5_pressed = 0
col6_pressed = 0
col7_pressed = 0
turn = 0

game_font = pygame.font.Font('assets/Game_font.ttf',50)

text_redwin = game_font.render('Player 1 WIN !', False, 'Red', 'Black')
text_bluewin = game_font.render('Player 2 WIN !', False, 'Blue', 'Black')
text_noonewin = game_font.render('No one win', False, 'Yellow', 'Black')

restart_button = game_font.render('Restart ?', False, 'White', 'Black')
restart_rect = restart_button.get_rect(topleft=(530, 420))

def check_all_move_played(matrix):
    if np.all(matrix != 6):
        return True
    else:
        return False


def check_win(matrix):
    # Check horizontal
    for row in range(6):
        for col in range(4):
            if matrix[row, col] == matrix[row, col+1] == matrix[row, col+2] == matrix[row, col+3] != 6:
                return True, matrix[row, col]

    # Check vertical
    for col in range(7):
        for row in range(3):
            if matrix[row, col] == matrix[row+1, col] == matrix[row+2, col] == matrix[row+3, col] != 6:
                return True, matrix[row, col]

    # Check diagonal (from top-left to bottom-right)
    for row in range(3):
        for col in range(4):
            if matrix[row, col] == matrix[row+1, col+1] == matrix[row+2, col+2] == matrix[row+3, col+3] != 6:
                return True, matrix[row, col]

    # Check diagonal (from bottom-left to top-right)
    for row in range(3, 6):
        for col in range(4):
            if matrix[row, col] == matrix[row-1, col+1] == matrix[row-2, col+2] == matrix[row-3, col+3] != 6:
                return True, matrix[row, col]

    return False, None



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if check_win(game_board)[0] or check_all_move_played(game_board):
                if restart_rect.collidepoint(mouse_pos):
                    game_board = np.full((6, 7), 6)
                    col1_pressed = 0
                    col2_pressed = 0
                    col3_pressed = 0
                    col4_pressed = 0
                    col5_pressed = 0
                    col6_pressed = 0
                    col7_pressed = 0
                    turn = 0
                continue
            if column_1.collidepoint(mouse_pos)and col1_pressed<6:
                if turn%2 == 0:
                    game_board[col1_pressed][0] = 0
                elif turn%2 == 1:
                    game_board[col1_pressed][0] = 1
                col1_pressed+=1
                turn +=1
            elif  column_2.collidepoint(mouse_pos)and col2_pressed<6:
                if turn%2 == 0:
                    game_board[col2_pressed][1] =0
                elif turn%2 == 1:
                    game_board[col2_pressed][1] = 1
                col2_pressed+=1
                turn += 1
            elif  column_3.collidepoint(mouse_pos)and col3_pressed<6:
                if turn%2 == 0:
                    game_board[col3_pressed][2] =0
                elif turn%2 == 1:
                    game_board[col3_pressed][2] = 1
                col3_pressed+=1
                turn +=1
            elif  column_4.collidepoint(mouse_pos)and col4_pressed<6:
                if turn %2== 0:
                    game_board[col4_pressed][3] =0
                elif turn%2 == 1:
                    game_board[col4_pressed][3] = 1
                col4_pressed+=1
                turn+=1
            elif  column_5.collidepoint(mouse_pos)and col5_pressed<6:
                if turn%2 == 0:
                    game_board[col5_pressed][4] =0
                elif turn%2 == 1:
                    game_board[col5_pressed][4] = 1
                col5_pressed+=1
                turn +=1
            elif  column_6.collidepoint(mouse_pos)and col6_pressed<6:
                if turn%2 == 0:
                    game_board[col6_pressed][5] =0
                elif turn%2 == 1:
                    game_board[col6_pressed][5] = 1
                col6_pressed+=1
                turn +=1
            elif  column_7.collidepoint(mouse_pos) and col7_pressed<6:
                if turn%2 == 0:
                    game_board[col7_pressed][6] =0
                elif turn%2 == 1:
                    game_board[col7_pressed][6] = 1
                col7_pressed+=1
                turn+=1
        
        if not check_win(game_board)[0] and not check_all_move_played(game_board):
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

            mouse_pos = pygame.mouse.get_pos()
            if column_1.collidepoint(mouse_pos):
                if (turn%2==0):
                    screen.blit(redtoken_surf, (300, 20))
                elif (turn%2==1):
                    screen.blit(bluetoken_surf, (300, 20))
            elif column_2.collidepoint(mouse_pos):
                if (turn%2==0):
                    screen.blit(redtoken_surf, (400, 20))
                elif (turn%2==1):
                    screen.blit(bluetoken_surf, (400, 20))
            elif column_3.collidepoint(mouse_pos):
                if (turn%2==0):
                    screen.blit(redtoken_surf, (500, 20))
                elif (turn%2==1):
                    screen.blit(bluetoken_surf, (500, 20))
            elif column_4.collidepoint(mouse_pos):
                if (turn%2==0):
                    screen.blit(redtoken_surf, (600, 20))
                elif (turn%2==1):
                    screen.blit(bluetoken_surf, (600, 20))
            elif column_5.collidepoint(mouse_pos):
                if (turn%2==0):
                    screen.blit(redtoken_surf, (700, 20))
                elif (turn%2==1):
                    screen.blit(bluetoken_surf, (700, 20))
            elif column_6.collidepoint(mouse_pos):
                if (turn%2==0):
                    screen.blit(redtoken_surf, (800, 20))
                elif (turn%2==1):
                    screen.blit(bluetoken_surf, (800, 20))
            elif column_7.collidepoint(mouse_pos):
                if (turn%2==0):
                    screen.blit(redtoken_surf, (900, 20))
                elif (turn%2==1):
                    screen.blit(bluetoken_surf, (900, 20))


            for col in range(7):
                    for row in range(6):
                        x_coord = 300 + col * 100
                        y_coord = (floor_rect.top - 80) - 100*row
                        if game_board[row][col] == 0:
                            screen.blit(redtoken_surf, (x_coord, y_coord))
                        elif game_board[row][col] == 1:
                            screen.blit(bluetoken_surf, (x_coord, y_coord))
        elif check_win(game_board)[0]:
            screen.blit(background_surf, (0,0))
            screen.blit(board_surf, board_rect)
            for col in range(7):
                    for row in range(6):
                        x_coord = 300 + col * 100
                        y_coord = (floor_rect.top - 80) - 100*row
                        if game_board[row][col] == 0:
                            screen.blit(redtoken_surf, (x_coord, y_coord))
                        elif game_board[row][col] == 1:
                            screen.blit(bluetoken_surf, (x_coord, y_coord))
            if turn%2==0:
                screen.blit(text_bluewin, (500, 320))
            elif turn%2==1:
                screen.blit(text_redwin, (500, 320))
            screen.blit(restart_button, restart_rect)

        elif check_all_move_played(game_board):
            screen.blit(background_surf, (0,0))
            screen.blit(board_surf, board_rect)
            for col in range(7):
                    for row in range(6):
                        x_coord = 300 + col * 100
                        y_coord = (floor_rect.top - 80) - 100*row
                        if game_board[row][col] == 0:
                            screen.blit(redtoken_surf, (x_coord, y_coord))
                        elif game_board[row][col] == 1:
                            screen.blit(bluetoken_surf, (x_coord, y_coord))
            screen.blit(text_noonewin, (520, 320))
            screen.blit(restart_button, restart_rect)
        print(check_win(game_board)[0] or check_all_move_played(game_board))
        pygame.display.update()
        clock.tick(60)




