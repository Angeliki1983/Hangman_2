while True:
    guess = input("Enter a single character: ")

    if guess == 1 and guess.isalpha():
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")