# Input: String -> letters, num, etc
# Output: list of letters
    # Lowercase
    # Letters alone
    # Sorted

def letter_extract(my_string):
    letter_list = []
    for ch in my_string:
        if ch.isalpha():
            if ch.lower() not in letter_list:
                letter_list.append(ch.lower())
    letter_list.sort()
    return letter_list
