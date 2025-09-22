# Hangman Game 🎯

A classic Hangman word-guessing game developed in Python, featuring a clean terminal interface, dynamic word selection, and attempt tracking. Perfect for practicing Python fundamentals like loops, conditionals, and string manipulation.

## Features ✨

- **Visual Hangman Display**: ASCII art showing hangman progression with each wrong guess
- **Clean Terminal Interface**: Automatic screen clearing for better user experience
- **Input Validation**: Comprehensive validation for single letters and duplicate prevention
- **Game Statistics**: Track victories and games played across sessions
- **Replay Functionality**: Option to play multiple games in succession
- **Multi-language Support**: Accepts 'yes/no' responses in English and French
- **Dynamic Word Selection**: Random word selection from predefined list

## Game Rules 📋

1. A random word is selected from the word list
2. You have **6 maximum errors** before losing
3. Guess letters one by one to reveal the hidden word
4. Correct guesses reveal letter positions
5. Wrong guesses add body parts to the hangman
6. Win by guessing all letters before the hangman is complete

## How to Play 🎮

1. Run the game: `python hangman.py`
2. Enter single letters when prompted
3. Watch the hangman drawing progress with wrong guesses
4. Try to guess the complete word before 6 errors
5. Choose to play again or quit after each game

## Technical Implementation 🔧

### Core Functions

- **`choose_word()`**: Randomly selects from predefined word list
- **`display_word(word, found_letters)`**: Shows current word state with guessed letters
- **`is_valid_letter(letter, proposed_letters)`**: Validates user input
- **`display_hangman(errors)`**: Returns ASCII art based on error count
- **`play_hangman()`**: Main game logic and loop
- **`ask_replay()`**: Handles replay functionality
- **`clear_terminal()`**: Cross-platform terminal clearing

### Word List
Current words: `python`, `program`, `hangman`, `algorithm`, `variable`

### Game States

**Hangman Progression (7 stages):**
1. Empty gallows
2. Head
3. Body
4. Left arm
5. Right arm
6. Left leg
7. Right leg (Game Over)

### Input Validation

- Single character only
- Alphabetic characters only
- No duplicate letters
- Case-insensitive input

## Game Flow 🔄

```
Start Game → Choose Random Word → Display Current State → 
Get User Input → Validate Input → Check Letter → 
Update Display → Check Win/Loss → Continue/End Game → 
Show Statistics → Ask Replay → Repeat/Exit
```

## User Interface Elements 🖥️

- **Visual Feedback**: ✅ for correct, ❌ for wrong guesses
- **Progress Tracking**: Shows errors (X/6) and proposed letters
- **Game Counter**: Displays current game number
- **Statistics**: Victory ratio across all games
- **Emojis**: Enhanced visual experience with relevant emojis

## Requirements 📦

- Python 3.x
- Standard library modules: `random`, `os`
- Terminal/Command prompt support

## Installation & Usage 🚀

```bash
# Clone or download the hangman.py file
# Navigate to the directory
cd path/to/hangman

# Run the game
python hangman.py
```

## Code Structure 📁

```
hangman.py
├── Utility Functions
│   ├── clear_terminal()     # Cross-platform screen clearing
│   └── choose_word()        # Random word selection
├── Display Functions
│   ├── display_word()       # Word state visualization
│   └── display_hangman()    # ASCII hangman art
├── Validation Functions
│   └── is_valid_letter()    # Input validation
├── Game Logic
│   ├── play_hangman()       # Main game loop
│   └── ask_replay()         # Replay functionality
└── Main Program
    └── main()               # Program entry point
```

## Game Statistics 📊

The game tracks:
- Total games played
- Number of victories
- Win/loss ratio
- Current game number

## Customization Options 🛠️

**Easy modifications:**
- Add more words to the `words` list in `choose_word()`
- Adjust `max_errors` to change difficulty
- Modify hangman ASCII art in `display_hangman()`
- Add different languages for replay prompts

## Educational Value 📚

**Python concepts demonstrated:**
- Functions and modular programming
- Loops (while, for)
- Conditional statements
- String manipulation
- Set operations
- List operations
- Random module usage
- OS module for system operations
- Input validation
- Game state management

## Future Enhancements 🚀

- Word categories/difficulty levels
- Hint system
- Save/load game progress
- Multiplayer functionality
- GUI version with tkinter
- Word definition display
- Custom word list import

---

**Enjoy playing Hangman! 🎉**