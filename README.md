# DIP392-01-34
An Applied System Software project.

Project document link: https://docs.google.com/document/d/1MmUNFiyZRnp19C-V46dIQ7F7v2JS4Yeuibsb75QsJ74/edit?usp=sharing 

Connect 4 Game

Overview:
This Connect 4 game is implemented using Python and the Pygame library. It follows an object-oriented design, separating game logic and display logic into two distinct classes: Connect4Game and Connect4Display. This modular design ensures ease of maintenance and potential for future extensions.

Requirements:
- Python 3.x
- Pygame library
- Numpy library

Installation:
1. Ensure you have Python 3 installed on your system.
2. Install the Pygame library: pip install pygame

Running the Game:
To run the game, execute the following command in your terminal:
python connect4.py


User Interaction:
1. Starting the Game: Upon running the script, the game window will open, displaying the Connect 4 board.
2. Making a Move:
   - Player 1 uses red tokens.
   - Player 2 uses blue tokens.
   - To make a move, click on the column where you want to drop your token. The token will be placed in the lowest available slot in that column.
3. Winning the Game: The game will automatically check for win conditions (four consecutive tokens horizontally, vertically, or diagonally). If a player wins, a message will be displayed on the screen.
4. Restarting the Game: If the game ends (either by a player winning or the board filling up), a "Restart?" button will appear. Click this button to reset the game and start a new match.

Classes and Responsibilities:
1. Connect4Game:
   - Manages the game state, including the board, player turns, and win conditions.
   - Methods include:
     - __init__(): Initializes the game board.
     - make_move(column): Updates the board with the player's move.
     - check_win(): Checks for win conditions.
     - is_full(): Checks if the board is full.
     - reset(): Resets the game state for a new match.

2. Connect4Display:
   - Handles the user interface and display logic using Pygame.
   - Methods include:
     - __init__(game): Initializes Pygame resources and links to the game logic.
     - run(): Main game loop that handles events, updates the game state, and renders the display.
     - draw_board(): Renders the game board and tokens.
     - handle_events(): Processes user inputs and updates the game state accordingly.
