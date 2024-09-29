# Tic Tac Toe Game

![Tic Tac Toe](https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Tic-tac-toe.svg/1200px-Tic-tac-toe.svg.png)

## Table of Contents

- [Tic Tac Toe Game](#tic-tac-toe-game)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Features](#features)
  - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Steps](#steps)
  - [Usage](#usage)
  - [Game Rules](#game-rules)
  - [File Structure](#file-structure)
    - [1. `tictactow.py`](#1-tictactowpy)
      - [**Key Components:**](#key-components)
    - [2. `tictactoe_records.json`](#2-tictactoe_recordsjson)
      - [**Structure:**](#structure)
    - [3. `README.md`](#3-readmemd)
    - [4. `LICENSE`](#4-license)
  - [Contributing](#contributing)
    - [**Guidelines:**](#guidelines)
  - [License](#license)
  - [Acknowledgements](#acknowledgements)
  - [Future Enhancements](#future-enhancements)
  - [Smart Opponent Option](#smart-opponent-option)
    - [Minimax Algorithm](#minimax-algorithm)
    - [How It Works](#how-it-works)
    - [Example](#example)
  - [Error Handling](#error-handling)
  - [Getting Started](#getting-started)
    - [Starting the Game](#starting-the-game)
    - [Sample Gameplay](#sample-gameplay)

## Overview

**Tic Tac Toe** is a classic command-line game where a player competes against the computer to align three of their symbols (X or O) in a row, column, or diagonal on a 3x3 grid. This Python implementation enhances user experience by simplifying input methods and maintaining game records using a JSON file.

## Features

- **Simplified Input:** Players enter a single number (1-9) to make their move, corresponding to grid positions.
- **Colored Interface:** Utilizes ANSI color codes for an engaging and visually appealing game board.
- **Persistent Records:** Tracks and stores game statistics such as player wins, computer wins, and ties in a `tictactoe_records.json` file.
- **Simple AI:** The computer opponent selects the first available spot on the board.
- **Smart AI:** Option to play against a smart opponent using the Minimax algorithm.
- **User-friendly Interface:** Clear prompts and informative messages guide the player throughout the game.

## Installation

### Prerequisites

- **Python 3.x** installed on your system. You can download it from [here](https://www.python.org/downloads/).

### Steps

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/tictactoe.git
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd tictactoe
   ```

3. **(Optional) Create a Virtual Environment:**

   It's good practice to use a virtual environment to manage dependencies.

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install Dependencies:**

   This project uses only standard Python libraries, so no additional installations are required.

## Usage

1. **Run the Game:**

   ```bash
   python tictactow.py
   ```

2. **Gameplay:**

   - Upon starting, the game board is displayed with numbered positions:

     ```
      1 | 2 | 3
     ---+---+---
      4 | 5 | 6
     ---+---+---
      7 | 8 | 9
     ```

   - **Player's Move:**
     - Enter a number between 1 and 9 to place your `X` in the corresponding position.
     - Example: Entering `5` places an `X` in the center.

   - **Computer's Move:**
     - The computer automatically places an `O` in the first available spot or uses the Minimax algorithm if playing as a smart opponent.

   - **Game Conclusion:**
     - The game announces the result (Player Wins, Computer Wins, or Tie) and displays updated scores.
     - You can choose to play again or exit.

3. **Exiting the Game:**

   - At any prompt, follow on-screen instructions to exit gracefully.

## Game Rules

1. **Objective:**
   - Align three of your symbols (`X`) horizontally, vertically, or diagonally.

2. **Gameplay:**
   - Players take turns placing their symbols on the grid.
   - The first player to align three symbols wins.
   - If all spots are filled without a winner, the game ends in a tie.

3. **Positions:**

   The grid positions are numbered as follows:

   ```
    1 | 2 | 3
   ---+---+---
    4 | 5 | 6
   ---+---+---
    7 | 8 | 9
   ```

## File Structure

````
tictactoe/
├── tictactow.py
├── tictactoe_records.json
├── README.md
└── LICENSE
````

### 1. `tictactow.py`

The main Python script that runs the Tic Tac Toe game. It handles game logic, user interactions, computer moves, and record-keeping.

#### **Key Components:**

- **Imports:**
  - `os`, `sys`, `json` for system operations and data handling.

- **ANSI Color Codes:**
  - Defines color schemes for an enhanced visual interface.

- **Game Board:**
  - Represents the 3x3 grid as a list of lists.

- **Records Management:**
  - Functions to load and save game statistics to `tictactoe_records.json`.

- **Game Functions:**
  - `clear_screen()`: Clears the console.
  - `render_board()`: Displays the current state of the board.
  - `check_winner()`: Determines if there's a winner or a tie.
  - `get_player_move()`: Handles player's input.
  - `get_computer_move()`: Logic for computer's move.
  - `is_valid_move(position)`: Validates player's chosen position.
  - `next_turn()`: Manages turn switching between player and computer.
  - `announce_result(result)`: Displays the game's outcome and updates records.
  - `reset_game()`: Resets the board for a new game.

- **Entry Point:**
  - Checks if the script is run as the main program and starts the game.

### 2. `tictactoe_records.json`

A JSON file that stores persistent game records, including the number of player wins, computer wins, and ties.

#### **Structure:**

```json
{
    "player_wins": 0,
    "computer_wins": 0,
    "ties": 0
}
````

- **Usage:**
  - The game reads from this file at startup to display existing records.
  - After each game, the results are updated and saved back to this file.

### 3. `README.md`

Provides an overview of the project, installation instructions, usage guidelines, and other relevant information.

### 4. `LICENSE`

Contains the licensing information for the project. Choose an appropriate license based on your preferences (e.g., MIT, GPL).

## Contributing

Contributions are welcome! If you'd like to enhance the game or fix issues, follow these steps:

1. **Fork the Repository:**

   Click the "Fork" button on the repository page to create your own copy.

2. **Create a New Branch:**

   ```bash
   git checkout -b feature/YourFeatureName
   ```

3. **Make Your Changes:**

   Implement your improvements or bug fixes.

4. **Commit Your Changes:**

   ```bash
   git commit -m "Add feature: Description of your feature"
   ```

5. **Push to Your Fork:**

   ```bash
   git push origin feature/YourFeatureName
   ```

6. **Create a Pull Request:**

   Navigate to your forked repository and click on "Compare & pull request" to submit your changes for review.

### **Guidelines:**

- **Code Style:** Follow PEP 8 guidelines for Python code.
- **Documentation:** Update the `README.md` and inline comments as needed.
- **Testing:** Ensure your changes do not break existing functionalities.

## License

[MIT License](LICENSE)

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Inspired by the classic Tic Tac Toe game.
- Utilizes standard Python libraries for simplicity and portability.
- Colors and UI enhancements inspired by ANSI color codes.

## Future Enhancements

- **Advanced AI:** Implement smarter algorithms for the computer opponent, such as the Minimax algorithm, to increase difficulty.
- **Graphical User Interface (GUI):** Develop a GUI version using libraries like Tkinter or PyGame for a more interactive experience.
- **Multiplayer Mode:** Allow two players to compete against each other on the same machine or over a network.
- **Move History:** Track and display the history of moves made during each game.
- **Customization:** Let players choose their symbols or the size of the grid.

---

## Smart Opponent Option

When the game starts, you will be prompted to choose whether you want to play against a smart opponent. If you choose 'yes', the computer will use the Minimax algorithm to make its moves, making it a challenging opponent.

### Minimax Algorithm

The Minimax algorithm is a recursive algorithm used in decision-making and game theory. It provides an optimal move for the player assuming that the opponent also plays optimally. In this Tic Tac Toe game, the Minimax algorithm is used to determine the best possible move for the computer when playing as a smart opponent.

### How It Works

1. **Recursive Evaluation:**
   - The algorithm recursively evaluates all possible moves and their outcomes.
   - It assigns a score to each move based on whether it leads to a win, loss, or tie.

2. **Maximizing and Minimizing:**
   - The computer (playing as 'O') tries to maximize its score.
   - The player (playing as 'X') tries to minimize the computer's score.

3. **Optimal Move Selection:**
   - The algorithm selects the move with the highest score for the computer and the lowest score for the player.

### Example

Here's an example of how the Minimax algorithm evaluates moves:

```
Initial Board:
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9

Player's Move: 5 (places 'X' in the center)

Board After Player's Move:
 1 | 2 | 3
---+---+---
 4 | X | 6
---+---+---
 7 | 8 | 9

Computer's Move: 1 (places 'O' in the top-left corner)

Board After Computer's Move:
 O | 2 | 3
---+---+---
 4 | X | 6
---+---+---
 7 | 8 | 9
```

The Minimax algorithm ensures that the computer makes the best possible move at each step, making it a formidable opponent.

## Error Handling

The game includes robust error handling to ensure a smooth user experience:

- **File Operations:**
  - Handles errors when reading from or writing to the records file.
- **Player Input:**
  - Validates player input to ensure it is a number between 1 and 9.
  - Prompts the player to enter a valid move if the input is invalid.
- **General Errors:**
  - Catches unexpected errors and exits the game gracefully with an appropriate message.

By incorporating these features, the Tic Tac Toe game provides a challenging and enjoyable experience for players, with options to play against a smart opponent and robust error handling to ensure smooth gameplay.

---

## Getting Started

Here's a quick example to get you started:

### Starting the Game

```bash
$ python tictactow.py
```

### Sample Gameplay

```
 Tic Tac Toe 

 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9

Enter your move (1-9): 5

 Tic Tac Toe 

 1 | 2 | 3
---+---+---
 4 | X | 6
---+---+---
 7 | 8 | 9

Computer has made a move.

 Tic Tac Toe 

 1 | 2 | 3
---+---+---
 4 | X | 6
---+---+---
 O | 8 | 9

Enter your move (1-9): 1

 Tic Tac Toe 

 X | 2 | 3
---+---+---
 4 | X | 6
---+---+---
 O | 8 | 9

Computer has made a move.

 Tic Tac Toe 

 X | 2 | 3
---+---+---
 4 | X | O
---+---+---
 O | 8 | 9

Enter your move (1-9): 9

 Tic Tac Toe 

 X | 2 | 3
---+---+---
 4 | X | O
---+---+---
 O | 8 | X

Player Wins!

Scores: Player - 1, Computer - 0, Ties - 0

Do you want to play again? (y/n):
```

Feel free to customize this documentation further to fit the specific nuances and features of your Tic Tac Toe game. Comprehensive documentation not only aids users but also attracts potential contributors, enhancing the overall quality and reach of your project.