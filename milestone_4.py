import random

# def check_guess(guess):
#     guess = guess.lower()

#     if guess in word:
#         print(f"Good guess! {guess} is in the word.")

#     else:
#         print(f"Sorry, {guess} is not in the word. Try again.")

# def ask_for_input():
#     while True:
#         guess = input("Enter a single character: ")

#         if len(guess) == 1 and guess.isalpha():
#             break
#         else:
#             print("Invalid letter. Please, enter a single alphabetical character.")

#     check_guess(guess) #Milestone 3/step 3

# ask_for_input()

class Hangman:
    def __init__(self, word_list, num_lives=5):#Mileston4/Task1/Step1,2,3
        self.word = random.choice(word_list) #1
        self.word_guessed = "_" * len(self.word) #2
        self.num_letters = len(set(self.word))#3
        self.num_lives = num_lives #4
        self.word_list = word_list
        self.list_of_guesses = []

#milestone 4/Task 2/Step 1

    def check_guess(self,guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")

    def ask_for_input(self):#Task 2/Step 2
        while True:#1
            guess = input("Guess a letter: ")#2
            if len(guess) != 1 or guess != guess.isalpha():#3
                print("Invalid letter. Please, enter a single alphabetical character.")#4
            elif guess in self.list_of_guesses:#5
                print("You've already tried that letter!")



    


word_list = ["apple", "banana","cherry","kiwi", "orange"]

word = random.choice(word_list)

print(word)