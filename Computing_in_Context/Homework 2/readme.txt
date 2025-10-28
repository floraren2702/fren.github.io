1. Secret Number Generation
In bulls_and_cows.py, the generate_secret() function creates a 4-digit string.

Using random.sample to pick 4 unique digits from 0–9, we ensure that there 
are no repeats. The digits are combined into a string to represent the 
secret number.

2. Counting Bulls
The how_many_bulls(guess, answer) function compares each digit of the player’s
guess with the secret number at the same index.

We find the number of bulls using a for loop that goes through each of the 
4 positions in the guess, and an if statement that checks if the digit in 
the guess matches the digit in the answer at the same index.
Every exact match increases the bull count by 1.

3. Counting Cows
The how_many_cows(guess, answer) function counts digits that are present in the
secret number but not in the same position. 

The program first records which digits are bulls and then excludes them from the
cow calculation. It loops through each position to record bulls so they won’t be
double-counted.

We use another for loop to check each digit of the guess. Within this loop, an 
if statement ensures three conditions: the digit exists somewhere in the answer,
it is not in the same position, and it has not already been counted as a bull.
Every match that meets these requirements increases the cow count by 1.

4. Gameplay Loop
In game.py, the play_game() function handles a single round.

A secret number is generated at the start, and the player is prompted
to enter a guess.

A while loop repeats until the player has correctly guessed the number.
After each guess, the program calls the helper functions to calculate 
bulls and cows, then prints the result. The loop continues until the guess
has 4 bulls, which means that the secret number was correctly guessed. 
The program also counts the number of attempts and displays it at the end.
