import pygame
import sys
import time
import tictactoe as ttt

pygame.init()
size = width, height = 600, 400

# Colors
background_color = (30, 30, 30)
line_color = (255, 255, 255)
button_color = (60, 60, 60)
button_hover_color = (100, 100, 100)
text_color = (255, 255, 255)
highlight_color = (0, 150, 136)

screen = pygame.display.set_mode(size)

mediumFont = pygame.font.SysFont("Open Sans", 28)
largeFont = pygame.font.SysFont("Open Sans", 40)
moveFont = pygame.font.SysFont("Open Sans", 60)

user = None
board = ttt.initial_state()
ai_turn = False

def draw_button(screen, rect, color, hover_color, text, font, mouse_pos):
    if rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, hover_color, rect, border_radius=8)
    else:
        pygame.draw.rect(screen, color, rect, border_radius=8)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

while True:
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(background_color)

    # Let user choose a player.
    if user is None:
        # Draw title
        title = largeFont.render("Play Tic-Tac-Toe", True, text_color)
        titleRect = title.get_rect(center=((width / 2), 50))
        screen.blit(title, titleRect)

        # Draw buttons
        playXButton = pygame.Rect((width / 8), (height / 2), width / 4, 50)
        playOButton = pygame.Rect(5 * (width / 8), (height / 2), width / 4, 50)
        draw_button(screen, playXButton, button_color, button_hover_color, "Play as X", mediumFont, mouse_pos)
        draw_button(screen, playOButton, button_color, button_hover_color, "Play as O", mediumFont, mouse_pos)

        # Check if button is clicked
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            if playXButton.collidepoint(mouse_pos):
                time.sleep(0.2)
                user = ttt.X
            elif playOButton.collidepoint(mouse_pos):
                time.sleep(0.2)
                user = ttt.O

    else:
        # Draw game board
        tile_size = 80
        tile_origin = (width / 2 - (1.5 * tile_size), height / 2 - (1.5 * tile_size))
        tiles = []
        for i in range(3):
            row = []
            for j in range(3):
                rect = pygame.Rect(tile_origin[0] + j * tile_size, tile_origin[1] + i * tile_size, tile_size, tile_size)
                pygame.draw.rect(screen, line_color, rect, 3, border_radius=8)

                if board[i][j] != ttt.EMPTY:
                    move = moveFont.render(board[i][j], True, text_color)
                    moveRect = move.get_rect(center=rect.center)
                    screen.blit(move, moveRect)
                row.append(rect)
            tiles.append(row)

        game_over = ttt.terminal(board)
        player = ttt.player(board)

        # Show title
        if game_over:
            winner = ttt.winner(board)
            if winner is None:
                title_text = "Game Over: Tie."
            else:
                title_text = f"Game Over: {winner} wins."
        elif user == player:
            title_text = f"Play as {user}"
        else:
            title_text = "Computer thinking..."
        title = largeFont.render(title_text, True, text_color)
        titleRect = title.get_rect(center=((width / 2), 30))
        screen.blit(title, titleRect)

        # Check for AI move
        if user != player and not game_over:
            if ai_turn:
                time.sleep(0.5)
                move = ttt.minimax(board)
                board = ttt.result(board, move)
                ai_turn = False
            else:
                ai_turn = True

        # Check for a user move
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1 and user == player and not game_over:
            for i in range(3):
                for j in range(3):
                    if board[i][j] == ttt.EMPTY and tiles[i][j].collidepoint(mouse_pos):
                        board = ttt.result(board, (i, j))

        if game_over:
            againButton = pygame.Rect(width / 3, height - 65, width / 3, 50)
            draw_button(screen, againButton, button_color, button_hover_color, "Play Again", mediumFont, mouse_pos)
            click, _, _ = pygame.mouse.get_pressed()
            if click == 1 and againButton.collidepoint(mouse_pos):
                time.sleep(0.2)
                user = None
                board = ttt.initial_state()
                ai_turn = False

    pygame.display.flip()
