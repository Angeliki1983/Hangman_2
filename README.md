
# Introduction

The Hangman Game:

This project is part of an exercise in AI Core designed to help learners practice fundamental Python concepts while also gaining familiarity with Git and GitHub. Hangman is a timeless game where one player selects a word(in this case this word is generated using import module, function "choice") and the other player attempts to guess it within a limited number of tries. In this implementation, the computer selects a word and the user endeavors to guess it.

# Table of Contents

1. [Overview of Hangman Game](#overview-of-hangman-game)
2. [Technologies Used](#technologies-used)
3. [Installation Instructions](#installation-instructions)
5. [File Structure of the Project](#file-structure-of-the-project)
   - [Milestone 2](#milestone-2)
   - [Milestone 3](#milestone-3)
   - [Milestone 4](#milestone-4)
   - [Milestone 5](#milestone-5)
6. [What I have learned/revised](#what-i-have-learned/revised)
   - [Milestone 1 & 2](#milestone-1--2)
   - [Milestone 3](#milestone-3)
   - [Milestone 4](#milestone-4)
   - [Milestone 5](#milestone-5)
7. [Recommended Improvements](#recommended-improvements)

# Technologies Used

- Python
- Git
- GitHub

---

# Installation instructions

**Clone the repository**: First, clone the repository from Github to your local machine. You can find more information by clicking on the link below:

```bash
https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository
```

You can also find a lot of relevant videos on Youtube on how to do that:

```bash
https://www.youtube.com/results?search_query=how+to+clone+a+repo+from+github+to+local+machine
```

**Navigate to the project directory:**
Move into the directory where the repository was cloned:
    ```
    cd your_folders'name
    ```

**Install dependancies:** Install the necessary packages using "pip".

```
pip install -r requirements.txt
```

**Recommended** :
It is good practice to create a virtual enviroment for your project to manage dependancies. Consider the operating system you are on (Windows or Macos/Linux) then activate the virtual enviroment using the relevant command.

**Run the game** :

 ```
python your_folders_name.py
```

Click on the link below for more information on how to download a github repository in your local machine:

 ```bash
 https://www.youtube.com/watch?v=ZFFtMyOFPe8&ab_channel=InfiniteCodes
 ```

# What I' ve learned/revised:

## Milestone 1 & 2

- **Importing the random Module**: Function that is used to generate random items from sequences , using the dot operator to access it's functions.In this case we used random.choice function that selects a random item form the sequence of favourite fruits.
- **Using the input() Function**: that takes input from the screen, returning the input in form of a string.
- **Command-Line Commands** :
  - **Creating a New File**: To create a new file using the touch command, ensure you are in the correct directory.

```
touch newfile.txt
```

- **Modifying Markdown Files in Visual Studio Code.**

You can find more information by clicking at the link below:

```
https://code.visualstudio.com/Docs/languages/markdown
```

or on several different Youtube videos.One of them I found particularly useful:

```
https://www.youtube.com/watch?v=DLLrcr9u_XI&ab_channel=DeAndreQueary
```

- Apply basic Python Syntax including variable assignment, list creating, modules, using loops(while),condition statements(if-else), list manipulation(using random.choice to select a word from the list),string manipulation(checking if a character is present in a string), Conditional logic(using if-else statements),loop control (using "while True" continues asking for user input until valid input is provided)

## Milestone 3

- Function definition and parameter passing:Defining functions allow us to encapsulate blocks of code for reusability and organisation.The parameter passing mechanism allow us to pass data into functions making them more versatile
- String manipulation:Converting strings into lower case using lower() method
- Calling functions in this case ask_for_input() and check_guess -->contains the main logic of the game prompting the user for input and cheking their guesses

## Milestone 4

<b>Task 3/Part 1</b>: asks us to create το loop through each letter in the word.In this case I used enumerate() built in function which allow us to loop over the iterable and have an automatic counter.It will return both the index and the value of the character in the list.

Using enumerate function we check each letter in the word to see if it matches the guessed letter.If it matches we need to update the corresponsing position in the 'word_guessed" hence why we need the index of the current letter(So that we know where to update the word_guessed) and the letter itself(to check if it matches the guessed letter).

for i, letter in enumerate(self.word)--->This line starts the loop where "i" will be the index and "letter" will be the actual character the user guesses at the index in self.word.

--->enumerate(self.word) -->This provides both index and letter for each iteration
example:

- First iteration "i" index is 0 LETTER is "a"
- Second iteration "i" index is 1 letter is "p"
- third iteration "i" index is 2 letter is "p"
- etc

With enumerate we can easily check if the "letter" is equal to "guess" and use "i" to update self.word_guessed at the current position.

<b>Part 2:</b>
Tasks requires to create an if statement that checks if the letter is equal to "guess".

After we iterate over each letter in self.word where "i" is the index and and letter is the actual characterof that index using the enumerate function, we check if the current letter matches the guessed letter.

---->if letter == guess:

- letter --> is the character in the word at the current index "i"
- guess --> is the letter that the player guessed

This line checks if the current "letter" is the same as the guess(the letter guess by the player)

 This part of the task has been a challenge. We are required to create an if block that replaces the corresponding "_" in the word_guessed with the guess. The hint provided proved out to be ery helpful--> Indexing the word_guessed at the position of the letter and assign it to the letter.(which is the users guess)

--->self.word_guessed[i] = guess : If "letter" matches "guess" means that the guessed letter is in the word at the position "i".Then update the self.word_guessed list at the index "i" to reveal the correctly guessed letter.

## EXAMPLE

Assuming that the random word generated is "apple" and the user guess is "p".

The loop (enumerate()) iterates over each letter in "apple":

- i = 0 -->letter = "a" (no match)
- i = 1 -->letter = "p" (match)
- i = 2 -->letter = "p" (match)
- i = 3 -->letter = "l" (no match)
- i = 4 -->letter = "e" (no match)

Condition : if letter == guess is True for indices i =1 and i = 2. The guessed letter "p" then is revealed in self.word_guessed at position 1 and 2.

<b>Part 3</b> Outside of the for -loop, reduce variable num_letters by 1

This line decreases the count of unique letters that are still left to guess.It helps keeping track of the players progress towards completing the word.

## EXAMPLE

1. ### Initialization

- Suppose the word guessed is "apple"
- Then self.word is "apple"
- self.num_letters = 4 (number of unique letters are 4)

2. ### Players guess

- Player guesses the letter "p"
- That means guess = p

3. ### Check if letter is in the word

- We check if the letter is in the word at /if guess in self.word/ line of code.In this  case where user guess is "p", condition evaluates as True because "p" is in the word "apple".

4. ### Update word_guessed

- The loop (for i, letter in enumerate(self.word)) checks each letter in the word "apple" and then updates the self.word_guessed exactly at the index where letter matches "p".

- self.word_guessed will look like this after the users guess --> ["-","p","p","-","-"]

5. ### Update num_letters

- self.num_letters -->decrease self.num_letters by 1

Before this line, self.num_letters was 4, after this line self.num_letters becomes 3

## Use of decreasing self.num_letters

is tracking the progress of the users as in how many unique letters the user still needs to guess. It gives an indication of how close the user is to winning the game.

#### When self.num_letters reaches 0 , means that the player has guessed all unique letters in the word and the user has won the game

## Showing current state of the word guessed

Providing visual feedback to the user using print("Word guessed by far: ", " ".join(self.word_guessed))--->joins the elements of the list self.word guessed into a single string with spaces between each character.

- self.word_guessed --->The list holds the current state of the word_guessed with correctly guessed letters at their respective positions and "_" underscores for letters that have not been guessed yet.

## Example

If the word to guess is "apple", user guess is "p" then the self.word_guessed is initialised to ["-", "p", "p", "-", "-"] . With "_".join(self.word_guessed) it prints out as word guessed by far: _ p p _ _

This line provides immediate visual feedback to the player about their progress. It joins the elements from the list into a string with spaces between elements.

<b>Task 7</b>

Task provides a list of recommended improvements such us:

- Meaningfull naming -->At this point, I have not yet made any changes
- Eliminate code dublication--> Removed print statement print(input("Word guessed by far: :") " ".join(self.word_guessed)), which provides a visual display of the letters guessed by far and the letter not yet guessed (replaced by underscores) from check_guess method and extracted the logic created a separate method called "word_guessed_display".  

# Milestone 5

### Task1/Step 1 &2 : 

Following exact instructions given by Step 1 and Step 2, I faced the problem where the game continued asking for an input after the number of lives reached zero. To fix this I had to add a "break" condition to break out of the loop when the game is over.

The flow before adding the "break"statement was causing the problem:

## Method: `ask_for_input`

### Flow without `break`:


```python
def ask_for_input(self):
    """Prompts the player to guess a letter and then handles input validation"""
    while True:  #1
        guess = input("Guess a letter: ")
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif guess in self.list_of_guesses:
            print("You've already tried that letter!")
        else:
            self.list_of_guesses.append(guess)
            self.check_guess(guess)
```

1. <b> Infinite loop: </b> The  `while true` creates an infinite loop, meaning it will continuously prompt the user to enter a letter.
2. <b> Input Validation: </b> Each iteration checks the validity of the input. If the input is invalid (not a single alphabetical character), it prompts the user again. If the input is already been guessed, it notifies the user they have already tried the letter.

If the "elif" block is not True(The letter guessed is not in the list of guesses then the next block is run  adding the guessed letter in the list of guessed letters(`self.list_of_guesses.append(guess)`), then running the `self.check_guesses(guess)` method to process the guess.

3. <b>Correct Input: </b> When valid and new letter is guessed it adds the guess to `self.list_of_guesses` and then calls the `self.check_guess` to proccess the guess.

## Issue 

After proccessing the guess the loop continues , it does not exit and will prompt the user guess immediately. The issue without the break statemtn is that it continues prompting the user after even a valid guess, and it will keep asking for guesses regardless of the game state. There is no  `break` condition to to exit the loop when the player has guesssed correctly or when the player has run out of lives within the `ask_for_input` method.

### Flow with  `break`:

Steps 1, 2, 3 above are the same. The difference is after processing the guess the `break` statement exits the loop, returning control back to the calling function `play_game`


# 
