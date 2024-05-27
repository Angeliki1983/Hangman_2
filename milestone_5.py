import random
class Hangman:
    
    def __init__(self, word_list, num_lives=5):
        """ Initializes new instance of the Hangman Game. Args --->word_list(is a list) : a list of words to chose from the game
        num_lives --> number of lives the player has defaults to 5"""
          
        self.word = random.choice(word_list) 
        self.word_guessed = ["_" for _ in self.word ]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives 
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self,guess):
        """Handling case insensive letters ,checks if the guessed letter is in the word. Updates the game accordingly.
        guess argument--> is the letter guessed"""
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i, letter in enumerate(self.word): 
                if letter == guess:
                    self.word_guessed[i] =guess 
            self.num_letters -= 1 
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
        self.word_guessed_displayed()
        
    def word_guessed_displayed(self):
        """Provides visual display of the letters guessed in the randomly guessed word by far"""
        print("Word guessed by far:", " ".join(self.word_guessed))
        

    def ask_for_input(self):
        """Prompts the player to guess a letter and then handles input validation"""
        while True:#1
            guess = input("Guess a letter: ")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You've already tried that letter!")
            else:
                self.list_of_guesses.append(guess) 
                self.check_guess(guess)

#Step 1 Create a function called play_game that takes word_list as a parameter
def play_game(word_list):
        # Create a variable called num_lives and assign it to 5
    num_lives = 5 # 1
    game = Hangman(word_list, num_lives) # 2,3

    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("You won the game!")
            break
                      



word_list = ["apple", "banana","cherry","kiwi", "orange"]

play_game(word_list)

    



