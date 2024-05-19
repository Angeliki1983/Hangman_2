import random
class Hangman:
    def __init__(self, word_list, num_lives=5):#Mileston4/Task1/Step1,2,3
        self.word = random.choice(word_list) #1
        self.word_guessed = ["_" for _ in self.word ]#2
        self.num_letters = len(set(self.word))#3
        self.num_lives = num_lives #4
        self.word_list = word_list
        self.list_of_guesses = []

#milestone 4/Task 2/Step 1

    def check_guess(self,guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            #iterate over each index and letter in the word:
            for i, letter in enumerate(self.word): # or for i in range(len(self.word))???
                if self.word[i] == guess:
                    #updating word_guessd_list with the correctly guessed letter
                    


    def ask_for_input(self):#Task 2/Step 2
        while True:#1
            guess = input("Guess a letter: ")#2
            if len(guess) == 1 or not guess.isalpha():#3
                print("Invalid letter. Please, enter a single alphabetical character.")#4
            elif guess in self.list_of_guesses:#5
                print("You've already tried that letter!")#6
            else:
                self.list_of_guesses.append(guess) #add guess to the list of guesses
                self.check_guess(guess)

#test game
word_list = ["apple", "banana","cherry","kiwi", "orange"]

Hangman_game = Hangman("apple")
Hangman_game.ask_for_input() #calling ask_for_input_function to start the game

    



