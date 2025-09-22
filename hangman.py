import random
import os

def clear_terminal():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def choose_word():
    """Chooses a random word from the predefined list"""
    words = ["python", "program", "hangman", "algorithm", "variable"]
    return random.choice(words)

def display_word(word, found_letters):
    """Displays the word with _ for letters not yet found"""
    display = ""
    for letter in word:
        if letter in found_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def is_valid_letter(letter, proposed_letters):
    """Checks if the input is a valid letter and not already proposed"""
    if len(letter) != 1:
        print("❌ Please enter a single letter.")
        return False
    if not letter.isalpha():
        print("❌ Please enter a letter from the alphabet.")
        return False
    if letter in proposed_letters:
        print("❌ You've already proposed this letter.")
        return False
    return True

def display_hangman(errors):
    """Display hangman progress (visual feedback)"""
    stages = [
        """
           -----
           |   |
               |
               |
               |
               |
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        """
    ]
    return stages[errors]

def ask_replay():
    """Ask the player if they want to play again"""
    while True:
        choice = input("\nWould you like to play again? (y/n): ").lower().strip()
        if choice in ['y', 'yes', 'oui', 'o']:
            return True
        elif choice in ['n', 'no', 'non', 'q', 'quit']:
            return False
        else:
            print("❌ Please enter 'y' for yes or 'n' for no.")

def play_hangman():
    """Main game function"""
    print("🎯 Welcome to Hangman!")
    print("Guess the word by proposing letters one by one.")
    print("You have a maximum of 6 errors.\n")
    
    # Game initialization
    word_to_guess = choose_word()
    found_letters = set()
    proposed_letters = set()
    errors = 0
    max_errors = 6
    
    # Main game loop
    while errors < max_errors:
        # Display current state
        print(display_hangman(errors))
        print(f"\nWord: {display_word(word_to_guess, found_letters)}")
        print(f"Proposed letters: {', '.join(sorted(proposed_letters))}")
        print(f"Errors: {errors}/{max_errors}")
        
        # Player input
        letter = input("\nEnter a letter: ").lower()
        
        # Clear terminal after each input to keep it clean
        clear_terminal()
        
        # Input validation
        if not is_valid_letter(letter, proposed_letters):
            continue
        
        # Add letter to proposed letters
        proposed_letters.add(letter)
        
        # Check if letter is in the word
        if letter in word_to_guess:
            found_letters.add(letter)
            print("✅ Correct letter!")
            
            # Check for victory
            if all(letter in found_letters for letter in word_to_guess):
                print(f"\n🎉 Congratulations! You found the word: {word_to_guess}")
                return True 
        else:
            errors += 1
            print("❌ Wrong letter!")
    
    # Game over - defeat
    print(display_hangman(errors))
    print(f"\n❌ Game over! The word was: {word_to_guess}")
    print("💀 You've been hanged!")
    return False 

def main():
    """Main program with replay functionality"""
    play_again = True
    games_played = 0
    victories = 0
    
    while play_again:
        games_played += 1
        clear_terminal()  
        
        print(f"{'='*40}")
        print(f"Game #{games_played}")
        print(f"{'='*40}")
        
        # Play one game
        victory = play_hangman()
        
        # Update victory count
        if victory:
            victories += 1
        
        # Display statistics
        print(f"\n📊 Statistics: {victories}/{games_played} victories")
        
        # Ask to play again
        play_again = ask_replay()
    
    clear_terminal()
    print("\n🎮 Thanks for playing Hangman!")
    print(f"Final score: {victories} victories out of {games_played} games")

# Game launch
if __name__ == "__main__":
    main()