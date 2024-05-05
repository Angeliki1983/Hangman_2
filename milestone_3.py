import random

word_list = ["apple", "banana","cherry","kiwi", "orange"]

word = random.choice(word_list)

print(word)

def check_guess(guess):#Task2/Step1

while True:
    guess = input("Enter a single character: ")

    if len(guess) == 1 and guess.isalpha():
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

if guess in word:#step /task 2
    print(f"Good guess! {guess} is in the word.")

else:
    print(f"Sorry, {guess} is not in the word. Try again.")


    