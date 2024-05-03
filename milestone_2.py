import random

word_list = ["apple", "banana","cherry","kiwi", "orange"]

word = random.choice(word_list)

print(word)

guess = input("Enter a single letter: ")

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")