import bulls_and_cows as bc

def main():
    # Please do not change this function!
    print('Welcome to Bulls and Cows death match!')
    again='y'
    while (again=='y'):
          play_game()
          again=input('would you like to play again? (y/n)')
    print('So long sucker!')


def play_game():
    ''' Plays a single interactive game of bulls and cows on the console'''
    # Generate a random secret number at the start of the game
    answer = bc.generate_secret()
    
    # Flag to keep track of whether the guess is correct
    correct_answer = False
    
    # Counter for how many guesses the player makes
    attempts = 0
    
    # Keep looping until the player guesses the correct number
    while correct_answer == False:
        guess = input("Enter a 4-digit number:") # Prompt the player for a guess
        # If the guess is not correct, check for bulls and cows
        if guess != answer:
            attempts += 1 # Increase attempt counter by 1
            # Use helper functions to count bulls and cows
            num_bulls = bc.how_many_bulls(guess, answer)
            num_cows = bc.how_many_cows(guess, answer)
            # Print the result with correct singular/plural wording
            if num_bulls == 1 and num_cows == 1:
                print(str(num_bulls) + " bull and " + str(num_cows) + " cow.")
            elif num_bulls == 1 and num_cows != 1:
                print(str(num_bulls) + " bull and " + str(num_cows) + " cows.")
            elif num_bulls != 1 and num_cows == 1:
                print(str(num_bulls) + " bulls and " + str(num_cows) + " cow.")
            else:
                print(str(num_bulls) + " bulls and " + str(num_cows) + " cows.")
        # If the guess matches the answer exactly, mark it correct and exit the loop
        else: 
            correct_answer = True
    
    # When the loop ends, print how many attempts it took to win
    print("You took " + str(attempts) + " attempts to guess the right number.")
            

#call the main function to run the game
main()
