# Write a function that counts the number of "a"s in a string.
# Already completed for you:
def count_as(s):
    count = 0
    for char in s:
        if char == "a":
            count = count + 1
    return count

# Write a function that returns true if the number of "a"s in a string is greater than the number of "b"s.
# already completed for you:
def more_as_than_bs(s):
    count_a = 0
    count_b = 0
    for char in s:
        if char == "a":
            count_a += 1
        elif char == "b":
            count_b += 1
    return count_a > count_b


# This solution assumes a singular word input!

my_dict = {} # creates empty dictionary
user_input = input("Give me a word! ")

# iterates over each letter of the user's word and puts into dictionary
# each key:value pairing indicates letter:frequency
# if there's already a dict entry for that letter (key), 
# just increment its count (value).
# otherwise, add a new entry with a count of 1
for letter in user_input:
    if letter in my_dict:
        my_dict[letter] += 1    
    else:
        my_dict[letter] = 1

letter_most = ""    # tracks the most frequent letter (key)
frequency_most = 0      # tracks the numerical frequency of that letter (value)

# iterates over the dictionary and finds the highest value
# updates variables each time a higher value is found
for item in my_dict:
    if my_dict[item] > frequency_most:
        frequency_most = my_dict[item]
        letter_most = item

print("The most frequent letter is", letter_most, "!")




# more robust solution that strips whitespace characters
# and mitigates repeats in upper/lowercase letters!

my_dict = {}
user_input = input("Now give me any string! ")

# places any non-whitespace character into dictionary
# converts letters to lowercase to avoid repeats
for ch in user_input:
    ch = ch.lower()
    if ch.isalpha():
        if ch in my_dict:
            my_dict[ch] += 1    
        else:
            my_dict[ch] = 1

character_most = ""
frequency_most = 0

for item in my_dict:
    if my_dict[item] > frequency_most:
        frequency_most = my_dict[item]
        character_most = item

print("The most frequent character is", character_most, "!")



serial_num = input("Enter the serial number on your bill: ")
if (serial_num[0] == serial_num[7] and serial_num[1] == serial_num[6]) and (
    serial_num[2] == serial_num[5] and serial_num[3] == serial_num[4]):
    print("Palindrome!")
elif (serial_num[0] == serial_num[3] and serial_num[1] == serial_num[2]) or (
    serial_num[4] == serial_num[7] and serial_num[5] == serial_num[6]):
    print("Partial Palindrome!")
if (serial_num[0] == "0" and serial_num[1] == "0") and (
    serial_num[2] == "0" and serial_num[3] == "0" and serial_num[4] == "0"):
    print("Low Number!")
elif serial_num[0] == "9":
    print("High Number!")
four_in_a_row = False
for i in range(5):
    if (serial_num[i] == serial_num[i+1]) and (
        serial_num[i+1] == serial_num[i+2] and serial_num[i+2] == serial_num[i+3]):
        four_in_a_row = True
if four_in_a_row == True:
    print("Four in a row!")



n = input("Enter a 9-digit number where no digit appears twice: ")

acceptable_answer = False
test = int(n)
while test <= 999999999 and acceptable_answer == False:
    test+=1
    original_numbers = list(n)
    for i in list(str(test)):
        if i in original_numbers:
            original_numbers.remove(i)
    if len(original_numbers) == 0:
        acceptable_answer = True
        print(test)

if acceptable_answer == False:
    print("Unacceptable answer!")


#BULLS AND COWS

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