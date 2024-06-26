# Tic-Tac-Toe Game (TASK 2)

This project implements a graphical version of the classic Tic-Tac-Toe game using Python and the Pygame library. It also includes an AI opponent that uses the Minimax algorithm with alpha-beta pruning to play optimally.

## Project Structure

The project contains two main files:
- `app.py`: This file contains the code for the graphical user interface and game logic.
- `tictactoe.py`: This file contains the core logic for the Tic-Tac-Toe game, including the Minimax algorithm with alpha-beta pruning.

## Requirements

- Python 3.x
- Pygame library

## Minimax Algorithm with Alpha-Beta Pruning

The Minimax algorithm is used to determine the optimal move for the AI. It is implemented with alpha-beta pruning to improve efficiency. The algorithm consists of:

- **max_alpha_beta_pruning**: Evaluates the maximum value a player can achieve.
- **min_alpha_beta_pruning**: Evaluates the minimum value a player can achieve.

