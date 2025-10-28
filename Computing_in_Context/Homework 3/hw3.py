# Problem 1 Part 1

def unique_letters(s):
    # Create empty list to store unique letters
    letter_list = []
    # Loop through each character in input string
    for ch in s:
        # Check if character is a letter (ignores punctuation and non-letters)
        if ch.isalpha():
            # Convert letter to lowercase
            ch = ch.lower()
            # Add letter only if it’s not already in the list
            if ch not in letter_list:
                letter_list.append(ch)
    # Sort list alphabetically
    letter_list.sort() 
    return letter_list

# Problem 1 Part 2

def unique_letters2(s):
    # Create empty set to automatically remove duplicates
    letter_set = set()
    # Loop through each character in input string
    for ch in s:
        # Check if character is a letter (ignores punctuation and non-letters)
        if ch.isalpha():
            # Convert letter to lowercase
            ch = ch.lower()
            # Add letter to set
            letter_set.add(ch)
    # Convert set back to a list
    letter_set_list = list(letter_set)
    # Sort list alphabetically
    letter_set_list.sort()
    return letter_set_list

# Problem 2 Part 1

def convert_list(input_file, output_file):
    # Open input file for reading
    with open(input_file, 'r') as file:
        # Create output file for writing
        with open(output_file, 'w') as newfile:
            # Read each word (line) from input file
            for line in file:
                # Remove newline
                word = line.strip()
                # Keep only words made of letters (ignores punctuation and non-letters)
                if word.isalpha():
                    # Convert word to lowercase
                    word = word.lower()
                    # Write the word to the file and move to a new line
                    newfile.write(word + "\n")

# Problem 2 Part 2 

def length_n(file_name,n):
    # Create list to store words with length n
    length_n_list = []
    # Open file for reading
    with open(file_name, 'r') as file:
        # Read each word (line) from input file
        for line in file:
            # Remove newline
            word = line.strip()
            # Add word if it matches length n
            if len(word) == n:
                length_n_list.append(word)
    return length_n_list

def starts_with(file_name, n, first_letter):
    # Create a list to store words with length n starting with first letter
    starts_with_list = []
    # Open file for reading
    with open(file_name, 'r') as file:
        # Read each word (line) from input file
        for line in file:
            # Remove newline
            word = line.strip()
            # Add word if it matches both length n and first letter
            if len(word) == n and word[0] == first_letter:
                starts_with_list.append(word)
    return starts_with_list

def contains_letter(file_name, n, included):
    # Create list to store words with length n and containing letter included
    contains_letter_list = []
    # Open file for reading
    with open(file_name, 'r') as file:
        # Read each word (line) from input file
        for line in file:
            # Remove newline
            word = line.strip()
            # Add word if it matches length n and 
            # contains letter included but does not start with it
            if len(word) == n and word[0] != included and included in word:
                contains_letter_list.append(word)
    return contains_letter_list

def vowel_heavy(file_name, n, m):
    # Create list to store vowel-heavy words
    vowel_heavy_list = []
    # Define set of vowels to check
    vowels = "aeiou"
    # Open file for reading
    with open(file_name, 'r') as file:
        # Read each word (line) from input file
        for line in file:
            # Remove newline
            word = line.strip()
            # Check word only if it matches length n
            if len(word) == n:
                count = 0
                # Count how many vowels are in word
                for letter in word:
                    if letter in vowels:
                        count += 1
                # Add word if it contains at least m vowels
                if count >= m:
                    vowel_heavy_list.append(word)
    return vowel_heavy_list