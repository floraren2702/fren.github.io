from lab4 import hamming_distance

def test_hamming_distance():
    assert hamming_distance("1 0 0 1 1", "1 0 1 0 0") == 3
    assert hamming_distance("Helloo", "Helium") == 3
    assert hamming_distance("abcde", "abzde") == 1
    assert hamming_distance("ab", "a") == "Invalid, the strings should be the same length"

from lab4 import is_palindrome

def test_is_palindrome():
    assert is_palindrome("madam") == True
    assert is_palindrome("loyal") == False
    assert is_palindrome("racecar") == True
    assert is_palindrome("abba") == True

