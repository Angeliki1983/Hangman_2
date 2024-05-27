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
                if letter == guess:#if the current letter matches the guessed letter
                #updating word_guessd_list with the correctly guessed letter
                    self.word_guessed[i] =guess ## Replace the corresponding "_" in word_guessed with the guessed letter
            self.num_letters -= 1 #decrease the number of guessed letters left to guess/reduce the variable num_letters by 1
        else:#milestone4 4/Task 4/step 1 & 2
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")



    def ask_for_input(self):#Task 2/Step 2
        while True:#1
            guess = input("Guess a letter: ")#2
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")#4
            elif guess in self.list_of_guesses:#5
                print("You've already tried that letter!")#6
            else:
                self.list_of_guesses.append(guess) #add guess to the list of guesses
                self.check_guess(guess)

#test game
word_list = ["apple", "banana","cherry","kiwi", "orange"]

Hangman_game = Hangman(word_list)
Hangman_game.ask_for_input() #calling ask_for_input_function to start the game

    



