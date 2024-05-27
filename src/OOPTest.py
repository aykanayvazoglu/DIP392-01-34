import pygame
import numpy as np
from sys import exit

class Connect4Game:
    def __init__(self):
        self.game_board = np.full((6, 7), 6)
        self.turn = 0
        self.col_pressed = [0] * 7  # Tracks the number of tokens in each column

    def reset(self):
        self.game_board = np.full((6, 7), 6)
        self.turn = 0
        self.col_pressed = [0] * 7

    def check_all_move_played(self):
        return np.all(self.game_board != 6)

    def check_win(self):
        # Check horizontal
        for row in range(6):
            for col in range(4):
                if self.game_board[row, col] == self.game_board[row, col+1] == self.game_board[row, col+2] == self.game_board[row, col+3] != 6:
                    return True, self.game_board[row, col]

        # Check vertical
        for col in range(7):
            for row in range(3):
                if self.game_board[row, col] == self.game_board[row+1, col] == self.game_board[row+2, col] == self.game_board[row+3, col] != 6:
                    return True, self.game_board[row, col]

        # Check diagonal (from top-left to bottom-right)
        for row in range(3):
            for col in range(4):
                if self.game_board[row, col] == self.game_board[row+1, col+1] == self.game_board[row+2, col+2] == self.game_board[row+3, col+3] != 6:
                    return True, self.game_board[row, col]

        # Check diagonal (from bottom-left to top-right)
        for row in range(3, 6):
            for col in range(4):
                if self.game_board[row, col] == self.game_board[row-1, col+1] == self.game_board[row-2, col+2] == self.game_board[row-3, col+3] != 6:
                    return True, self.game_board[row, col]

        return False, None

    def play_move(self, column):
        if self.col_pressed[column] < 6:
            self.game_board[self.col_pressed[column]][column] = self.turn % 2
            self.col_pressed[column] += 1
            self.turn += 1
            return True
        return False

class Connect4Display:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption('Connect 4')
        self.clock = pygame.time.Clock()

        self.column_rects = [pygame.Rect(292 + i * 100, 0, 95, 720) for i in range(7)]
        self.floor_rect = pygame.Rect(0, 709, 1280, 11)

        self.background_surf = pygame.image.load('assets/bg.jpg').convert()
        self.board_surf = pygame.image.load('assets/connect4Board.png').convert()
        self.board_rect = self.board_surf.get_rect(midbottom=(640, 720))

        self.redtoken_surf = pygame.image.load('assets/redtoken.png')
        self.bluetoken_surf = pygame.image.load('assets/bluetoken.png')

        self.game_font = pygame.font.Font('assets/Game_font.ttf', 50)
        self.text_redwin = self.game_font.render('Player 1 WIN !', False, 'Red', 'Black')
        self.text_bluewin = self.game_font.render('Player 2 WIN !', False, 'Blue', 'Black')
        self.text_noonewin = self.game_font.render('No one win', False, 'Yellow', 'Black')
        self.restart_button = self.game_font.render('Restart ?', False, 'White', 'Black')
        self.restart_rect = self.restart_button.get_rect(topleft=(530, 420))

        self.game = Connect4Game()

    def draw(self):
        self.screen.blit(self.background_surf, (0, 0))
        self.screen.blit(self.board_surf, self.board_rect)
        for col in range(7):
            for row in range(6):
                x_coord = 300 + col * 100
                y_coord = (self.floor_rect.top - 80) - 100 * row
                if self.game.game_board[row][col] == 0:
                    self.screen.blit(self.redtoken_surf, (x_coord, y_coord))
                elif self.game.game_board[row][col] == 1:
                    self.screen.blit(self.bluetoken_surf, (x_coord, y_coord))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.game.check_win()[0] or self.game.check_all_move_played():
                        if self.restart_rect.collidepoint(mouse_pos):
                            self.game.reset()
                        continue
                    for i, column in enumerate(self.column_rects):
                        if column.collidepoint(mouse_pos):
                            self.game.play_move(i)
                            break

            self.draw()
            if not self.game.check_win()[0] and not self.game.check_all_move_played():
                mouse_pos = pygame.mouse.get_pos()
                for i, column in enumerate(self.column_rects):
                    if column.collidepoint(mouse_pos):
                        if self.game.turn % 2 == 0:
                            self.screen.blit(self.redtoken_surf, (300 + i * 100, 20))
                        else:
                            self.screen.blit(self.bluetoken_surf, (300 + i * 100, 20))
            elif self.game.check_win()[0]:
                winner = self.game.check_win()[1]
                self.screen.blit(self.text_bluewin if winner == 1 else self.text_redwin, (500, 320))
                self.screen.blit(self.restart_button, self.restart_rect)
            elif self.game.check_all_move_played():
                self.screen.blit(self.text_noonewin, (520, 320))
                self.screen.blit(self.restart_button, self.restart_rect)

            pygame.display.update()
            self.clock.tick(60)

if __name__ == "__main__":
    game_display = Connect4Display()
    game_display.run()
