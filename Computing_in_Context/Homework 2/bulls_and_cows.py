import random

def generate_secret():
    ''' Generates a 4 digit number with no repeat digits''
    It converts the number to a string and returns it'''
    
    # Create a list of digits 1 to 9
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    # Select 4 unique digits at random
    secret_list = random.sample(digits, 4)

    # Combine the 4 digits into a string
    secret = secret_list[0] + secret_list[1] + secret_list[2] + secret_list[3]
    return secret

def how_many_bulls(guess,answer):
    ''' Returns the number of bulls as an int that the guess earns when the
    secret number is answer. answer and guess should be strings'''
    
    # Start a counter at 0 to track the number of bulls found
    bulls = 0

    # Loop through each of the 4 positions in the guess 
    # Check if the digit at position i in the guess matches
    # the digit at position i in the answer.
    for i in range(4):
        if guess[i] == answer[i]:
            bulls += 1
    return bulls

def how_many_cows(guess,answer):
    ''' Returns the number of cows as an int that the guess earns when the
    secret number is answer. answer and guess should be strings'''
    
    # Start a counter at 0 to track the number of cows found
    cows = 0
    # List to record digits already identified as bulls
    bulls = []

    # First, identify bulls so they won’t be counted as cows later
    for i in range(4):
        if guess[i] == answer[i]:
            bulls.append(guess[i]) # Store the digit that matched exactly
    # Loop through each of the 4 positions in the guess 
    # Check if the digit at position i in the guess matches one
    # of the digits in the answer, but is not in the same position
    # and was not already recorded as a bull digit
    for i in range(4):
        if guess[i] in answer and guess[i] != answer[i] and guess[i] not in bulls:
            cows += 1
    return cows