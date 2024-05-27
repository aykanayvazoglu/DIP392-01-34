import sys
import pygame
import numpy as np

class Connect4Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption('Connect 4')
        self.clock = pygame.time.Clock()

        self.columns = [pygame.Rect(x, 0, 95, 720) for x in range(292, 892 + 1, 100)]

        self.background_surf = pygame.image.load('assets/bg.jpg').convert()
        self.window_icon = pygame.image.load('assets/icon.png')
        pygame.display.set_icon(self.window_icon)

        self.board_surf = pygame.image.load('assets/connect4Board.png').convert()
        self.board_rect = self.board_surf.get_rect(midbottom=(640, 720))

        self.redtoken_surf = pygame.image.load('assets/redtoken.png')
        self.bluetoken_surf = pygame.image.load('assets/bluetoken.png')

        self.floor_rect = pygame.Rect(0, 709, 1280, 11)

        self.game_board = np.full((6, 7), 6)
        self.column_pressed = [0] * 7
        self.turn = 0

        self.game_font = pygame.font.Font('assets/Game_font.ttf', 50)
        self.text_redwin = self.game_font.render('Player 1 WIN !', False, 'Red', 'Black')
        self.text_bluewin = self.game_font.render('Player 2 WIN !', False, 'Blue', 'Black')
        self.text_noonewin = self.game_font.render('No one win', False, 'Yellow', 'Black')

        self.restart_button = self.game_font.render('Restart ?', False, 'White', 'Black')
        self.restart_rect = self.restart_button.get_rect(topleft=(530, 420))

    def check_all_move_played(self):
        return np.all(self.game_board != 6)

    def check_win(self):
        matrix = self.game_board
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

    def restart_game(self):
        self.game_board = np.full((6, 7), 6)
        self.column_pressed = [0] * 7
        self.turn = 0

    def handle_mouse_click(self, mouse_pos):
        if self.check_win()[0] or self.check_all_move_played():
            if self.restart_rect.collidepoint(mouse_pos):
                self.restart_game()
            return

        for idx, column in enumerate(self.columns):
            if column.collidepoint(mouse_pos) and self.column_pressed[idx] < 6:
                self.game_board[self.column_pressed[idx]][idx] = self.turn % 2
                self.column_pressed[idx] += 1
                self.turn += 1
                break

    def draw_tokens(self):
        for col in range(7):
            for row in range(6):
                x_coord = 300 + col * 100
                y_coord = (self.floor_rect.top - 80) - 100 * row
                if self.game_board[row][col] == 0:
                    self.screen.blit(self.redtoken_surf, (x_coord, y_coord))
                elif self.game_board[row][col] == 1:
                    self.screen.blit(self.bluetoken_surf, (x_coord, y_coord))

    def draw_game(self):
        self.screen.blit(self.background_surf, (0, 0))
        self.screen.blit(self.board_surf, self.board_rect)
        self.draw_tokens()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_mouse_click(pygame.mouse.get_pos())

            if not self.check_win()[0] and not self.check_all_move_played():
                self.screen.fill((0, 0, 0))
                self.draw_game()
                mouse_pos = pygame.mouse.get_pos()
                for idx, column in enumerate(self.columns):
                    if column.collidepoint(mouse_pos):
                        if self.turn % 2 == 0:
                            self.screen.blit(self.redtoken_surf, (300 + idx * 100, 20))
                        else:
                            self.screen.blit(self.bluetoken_surf, (300 + idx * 100, 20))
                        break
            elif self.check_win()[0]:
                self.draw_game()
                if self.turn % 2 == 0:
                    self.screen.blit(self.text_bluewin, (500, 320))
                else:
                    self.screen.blit(self.text_redwin, (500, 320))
                self.screen.blit(self.restart_button, self.restart_rect)
            elif self.check_all_move_played():
                self.draw_game()
                self.screen.blit(self.text_noonewin, (520, 320))
                self.screen.blit(self.restart_button, self.restart_rect)

            pygame.display.update()
            self.clock.tick(60)

if __name__ == "__main__":
    Connect4Game().run()
