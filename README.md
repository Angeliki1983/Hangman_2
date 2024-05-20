# Introduction
The Hangman Game: 

This project is part of an exercise in AI Core designed to help learners practice fundamental Python concepts while also gaining familiarity with Git and GitHub. Hangman is a timeless game where one player selects a word and the other player attempts to guess it within a limited number of tries. In this implementation, the computer selects a word and the user endeavors to guess it.


# Table of Contents:

Overview of Hangman Game
Hangman is a classic word-guessing game where one player thinks of a word and the other player attempts to guess it within a limited number of tries.

# Technologies Used:
- Python
- Git
- GitHub

---
- Installation instructions:---> To be updatedclone repo from my account to your local memory-->provide instructions
- Usage instructions :--->To be updated
- File structure of the project --->to be updated
- License information

# What I ve learned/revised:

## Milestone 1 & 2 & 3 :

- Import module random -->Function that is used to generate random items form sequences , with dot operator to acces its functions.In this case we used random.choice function that selects a random item form the sequence of favourite fruits.
- input() function-->that takes input from the screen, returning the input in form of a string
- touch command to create a new file also making sure to have navigated in the correct directory
- Modifying markdown files using Visual code(in this case README.md) which usually includes information about the project description, installation, usage examples .etc Also using "Preview on the side" on the upper right corner of my IDE to have a preview of the markdown file and how it will appear in my remote repo.
- Create a lsit of dots in a markdown file using "-" or "*", creating ordered lists.
- Push changes on Github via interfrated terminal
- Simplify logic by moving code blocks by encapsulating the logical repetition into a single function
- Apply basic Python Syntax including variable assignment, list creating, modules, using loops(while),condition statements(if-else), list manipulation(using random.choice to select a word from the list),string manipulation(checking if a character is present in a string), Conditional logic(using if-else statements),loop control (continues user input until valid input is provided)
## Milestone 3 :

- Function definition and parameter passing:Defining functions allow us to encapsulate blocks of code for reusability and organisation.The parameter passing mechanism allow us to pass data into functions making them more versatile 
- String manipulation:Converting strings into lower case using lower() method
- Gaining familiarity with common programming constructs
- Calling functions in this case ask_for_input() and check_guess -->contains the main logic of the game prompting the user for input and cheking their guesses

## Milestone 4:
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

<b>Part 3</b> This part of the task has been a challenge. We are required to create an if block that replaces the corresponding "_" in the word_guessed with the guess. The hint provided proved out to be ery helpful--> Indexing the word_guessed at the position of the letter and assign it to the letter.(which is the users guess)

--->self.word_guessed[i] = guess : If "letter" matches "guess" means that the guessed letter is in the word at the position "i".Then update the self.word_guessed list at the index "i" to reveal the correctly guessed letter.

## EXAMPLE:
Assuming that the random word generated is "apple" and the user guess is "p".

The loop (enumerate()) iterates over each letter in "apple":

- i = 0 -->letter = "a" (no match)
- i = 1 -->letter = "p" (match)
- i = 2 -->letter = "p" (match)
- i = 3 -->letter = "l" (no match)
- i = 4 -->letter = "e" (no match)

Condition : if letter == guess is True for indices i =1 and i = 2. The guessed letter "p" then is revealed in self.word_guessed at position 1 and 2.




